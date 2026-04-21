import pygame
import time
import random

from libs.system_lib import System, Background
from libs.components.ui import Button, HealthBar, StaminaBar, BossHealthBar
from libs.sprites.player import Player
from libs.sprites.enemy import Enemy, SkeletonEnemy, GoblinEnemy, MushroomEnemy, BigMushroomEnemy, FlyingEyeEnemy
from libs.sprites.boss import MinotaurEnemy, GolemEnemy, TarnishedWidowEnemy

from ..db.statisticDb import GameDB
from ..db.playerDb import PlayerStats

from ..db.additional_db import EnemyDefeated, InGameTimeStamp

from ..stat import player, lv1_sts, lv2_sts, lv3_sts, lv4_sts, lv5_sts, minotaur, stone_golem, tarnished_widow

MULTT = 440

LOWEST_SPAWN = 15
HIGHT_SPAWN = 20


from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_LSHIFT,
    K_SPACE,
    MOUSEBUTTONDOWN,
    K_r,
    K_f,
)

# this_db = gameDB(['a', 'b', 'c'], 'test')
# this_db.insert_data('a', 1, 1)

class Level:
    def __init__(self, sys, screen, current_lv):
        self.sys = sys
        self.screen = screen
        self.current_lv = current_lv
        
        self.ambient = None
        self.bg = None

        self.enemy_to_spawn_l = []
        self.enemy_to_spawn_r = []

        self.level_boss = []

        self.hit_sound = pygame.mixer.Sound(("./sounds/player/flesh_swing.mp3"))
        self.hit_sound.set_volume(0.4)

        self.spw_mul_l = 0
        self.spw_mul_r = 0

        self.enemies_hit_player = set()
        self.boss_hit_player = set()

        self.total_enemy = 0

        self.pass_round = [False, False] # enemy round / boss round
        self.damage_received = 0
        self.enemy_killed = 0
        self.point_earned = 0

        self.sts_operator = PlayerStats()
        self.stage_operator = GameDB()
        self.time_stamp_operator = InGameTimeStamp()
        self.enemy_defeated_operator = EnemyDefeated()

        # for time stamp
        self.last_print_time = 0
        self.interval = 5000
        self.curr_time = 0

        self.gennerate_enemy()
        if len(self.level_boss) == 0:
            self.gennerate_boss()
            # print(self.level_boss, 'BOSS GENNERATED')

        # print(f"IN LEVEL - {self.current_lv}")
    
    def show(self):
        self.level_selected()

        player_ = Player(self.sys)

        healthbar_ = HealthBar(self.screen, 30, 172, player['health'], 20, player_.health)
        staminabar_ = StaminaBar(self.screen, 30, 200, player['stamina'], 20, player_.stamina)

        # self.gennerate_enemy()
        # if len(self.level_boss) == 0:
        #     self.gennerate_boss()
        #     print(self.level_boss, 'BOSS SPAWNED')

        self.total_enemy = len(self.enemy_to_spawn_l) + len(self.enemy_to_spawn_r)
        # print(f"Total enemy -> {self.total_enemy}")
        
        # currently can create healthbar for only 1 boss
        for i in self.level_boss:
            if i.boss_class == "minotaur":
                boss_healthbar_ = BossHealthBar(self.screen, 285, 655, 700, 20, minotaur['health'])
            elif i.boss_class == "stone_golem":
                boss_healthbar_ = BossHealthBar(self.screen, 285, 655, 700, 20, stone_golem['health'])
            elif i.boss_class == "tarnished_widow":
                boss_healthbar_ = BossHealthBar(self.screen, 285, 655, 700, 20, tarnished_widow['health'])

        clock = pygame.time.Clock()

        running = True
        while running:
            dashing = False
            jump = False
            attack_click = False
            combo_click = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        result = self.pause(player_)
                        if result == "quit":
                            # self.ambient.stop()
                            self.ambient = None
                            running = False
                        
                    if event.key == K_SPACE or event.key == K_w:
                        # print("jumping")
                        jump = True
                    elif event.key == K_LSHIFT:
                        # print("dashing")
                        dashing = True
                    elif event.key == K_r:
                        attack_click = True
                    elif event.key == K_f:
                        combo_click = True

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        attack_click = True
                    else:
                        combo_click = True
                    # print(attack_click, combo_click)
                        
                elif event.type == QUIT:
                    result = self.pause(player_)
                    if result == "quit":
                        # self.ambient.stop()
                        self.ambient = None
                        running = False

            pressed_keys = pygame.key.get_pressed()
            player_.update(pressed_keys, dashing, jump, attack_click, combo_click)

            current_time = pygame.time.get_ticks()

            if player_.is_dead and player_.play_dead_anim:
                self.show_result(player_, True)
                player['accumulative_points'] += self.point_earned
                self.sts_operator.update(player['health'], player['power'], player['critical'], player['stamina'], player['stamina_regen'], player['accumulative_points'])
                if player_.health < 0:
                    player_.health = 0
                self.time_stamp_operator.update(player_.health, self.point_earned, self.curr_time)
                running = False
            
            self.screen.blit(self.bg, (0, 0))

            if len(self.enemy_to_spawn_l) + len(self.enemy_to_spawn_r) > 0:
                for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
                    for j in i:
                        j.update(player_.hitbox.centerx, player_.is_dead)
                        self.screen.blit(j.surf, j.rect)
                        if j.health <= 0 and not j.kill_counted:
                            j.kill_counted = True
                            self.enemy_killed += 1
                            self.point_earned += j.point
                            if j.__class__.__name__ == "SkeletonEnemy":
                                self.enemy_defeated_operator.update(1, 0, 0, 0, 0, 0, 0, 0)
                            elif j.__class__.__name__ == "GoblinEnemy":
                                self.enemy_defeated_operator.update(0, 1, 0, 0, 0, 0, 0, 0)
                            elif j.__class__.__name__ == "MushroomEnemy":
                                self.enemy_defeated_operator.update(0, 0, 1, 0, 0, 0, 0, 0)
                            elif j.__class__.__name__ == "BigMushroomEnemy":
                                self.enemy_defeated_operator.update(0, 0, 0, 1, 0, 0, 0, 0)
                            elif j.__class__.__name__ == "FlyingEyeEnemy":
                                self.enemy_defeated_operator.update(0, 0, 0, 0, 1, 0, 0, 0)

                self.check_attack_collide_enemy(player_)
                self.check_enemy_attack_collide_player(player_)

                self.enemy_to_spawn_l = [i for i in self.enemy_to_spawn_l if not i.complete_dead_animation]
                self.enemy_to_spawn_r = [i for i in self.enemy_to_spawn_r if not i.complete_dead_animation]
            else:
                self.pass_round = [True, False]

            if self.pass_round[0] == True:
                # print("boss")

                for i in self.level_boss:
                    i.update(player_.hitbox.centerx, player_.is_dead) # BOSSSSSS
                    self.screen.blit(i.surf, i.rect)

                    for rect in i.landing_box:
                        pygame.draw.rect(self.screen, (255, 50, 0), rect) # for warning incomming jump attack

                self.check_attack_collide_boss(player_)
                self.check_boss_attack_collide_player(player_)

                self.level_boss = [i for i in self.level_boss if not i.complete_dead_animation]

                for i in self.level_boss:
                    self.sys.paragraph(320, 625, 100, 100, f"{i.boss_name}", (255, 255, 255), 20)
                    boss_healthbar_.update_health(i.health)

                for i in self.level_boss:
                    if i.health <= 0 and not i.kill_counted:
                        i.kill_counted = True
                        self.point_earned += i.point
                        print(i.__class__.__name__)
                        if i.__class__.__name__ == "MinotaurEnemy":
                            self.enemy_defeated_operator.update(0, 0, 0, 0, 0, 1, 0, 0)
                        elif i.__class__.__name__ == "GolemEnemy":
                            self.enemy_defeated_operator.update(0, 0, 0, 0, 0, 0, 1, 0)
                        elif i.__class__.__name__ == "TarnishedWidowEnemy":
                            self.enemy_defeated_operator.update(0, 0, 0, 0, 0, 0, 0, 1)

            if self.pass_round[0] and len(self.level_boss) == 0:
                self.show_result(player_, False)
                player['accumulative_points'] += self.point_earned
                self.sts_operator.update(player['health'], player['power'], player['critical'], player['stamina'], player['stamina_regen'], player['accumulative_points'])
                running = False

            # self.show_hitboxes(player_) # hitboxes display -------------------------------- !!!!!!!!!!!
            healthbar_.update_health(player_.health)
            staminabar_.update_stamina(player_.stamina)
            # print(player_.health)

            if current_time - self.last_print_time >= self.interval:
                # print("time hitted !!!!")
                self.last_print_time = current_time
                if player_.health < 0:
                    player_.health = 0
                self.time_stamp_operator.update(player_.health, self.point_earned, self.curr_time) # ------------------ publish time stamp
                self.curr_time+=5
                # print(self.last_print_time)

            # self.sys.paragraph_normal(320, 200, 100, 100, f"{len(self.enemy_to_spawn_l)+len(self.enemy_to_spawn_r)}/{self.total_enemy}", (255, 255, 255), 60)
            self.screen.blit(player_.surf, player_.rect)

            clock.tick(60)
            
            pygame.display.flip()
            
    def level_selected(self):
        if self.bg == None:
            if self.current_lv == 1:
                self.bg = Background("stage", "s1").get_bg()
                # if self.ambient == None:
                    # self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg1.mp3")).play(loops=-1)
                    # self.ambient.set_volume(1.0)
            elif self.current_lv == 2:
                self.bg = Background("stage", "s2").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg2.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
            elif self.current_lv == 3:
                self.bg = Background("stage", "s3").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg3.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
            elif self.current_lv == 4:
                self.bg = Background("stage", "s4").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg4.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
            elif self.current_lv == 5:
                self.bg = Background("stage", "s5").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg5.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
        self.bg = pygame.transform.scale_by(self.bg, 1.1)

    def gennerate_enemy(self):
        try:
            if self.current_lv == 1:
                random_enemy = random.randint(LOWEST_SPAWN, HIGHT_SPAWN)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    this_enemy = random.choice(lv1_sts['enemy'])
                    if spawn_dir == 0:
                        pos_ = -300 + self.spw_mul_l
                    else:
                        pos_ = self.sys.w+120 + self.spw_mul_r

                    if this_enemy == "skeleton":
                        self.enemy_to_spawn_l.append(SkeletonEnemy(self.sys, pos_, 1))
                    elif this_enemy == "goblin":
                        self.enemy_to_spawn_l.append(GoblinEnemy(self.sys, pos_, 1))
                    elif this_enemy == "mushroom":
                        self.enemy_to_spawn_l.append(MushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "big_mushroom":
                        self.enemy_to_spawn_l.append(BigMushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "flying_eye":
                        self.enemy_to_spawn_l.append(FlyingEyeEnemy(self.sys, pos_, 1))

                    # self.total_enemy += 1

                    self.spw_mul_l -= MULTT
                    self.spw_mul_r += MULTT
            
            elif self.current_lv == 2:
                random_enemy = random.randint(LOWEST_SPAWN, HIGHT_SPAWN)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    this_enemy = random.choice(lv2_sts['enemy'])
                    if spawn_dir == 0:
                        pos_ = -300 + self.spw_mul_l
                    else:
                        pos_ = self.sys.w+120 + self.spw_mul_r

                    if this_enemy == "skeleton":
                        self.enemy_to_spawn_l.append(SkeletonEnemy(self.sys, pos_, 1))
                    elif this_enemy == "goblin":
                        self.enemy_to_spawn_l.append(GoblinEnemy(self.sys, pos_, 1))
                    elif this_enemy == "mushroom":
                        self.enemy_to_spawn_l.append(MushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "big_mushroom":
                        self.enemy_to_spawn_l.append(BigMushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "flying_eye":
                        self.enemy_to_spawn_l.append(FlyingEyeEnemy(self.sys, pos_, 1))

                    # self.total_enemy += 1
                    
                    self.spw_mul_l -= MULTT
                    self.spw_mul_r += MULTT

            elif self.current_lv == 3:
                random_enemy = random.randint(LOWEST_SPAWN, HIGHT_SPAWN)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    this_enemy = random.choice(lv3_sts['enemy'])
                    if spawn_dir == 0:
                        pos_ = -300 + self.spw_mul_l
                    else:
                        pos_ = self.sys.w+120 + self.spw_mul_r

                    if this_enemy == "skeleton":
                        self.enemy_to_spawn_l.append(SkeletonEnemy(self.sys, pos_, 1))
                    elif this_enemy == "goblin":
                        self.enemy_to_spawn_l.append(GoblinEnemy(self.sys, pos_, 1))
                    elif this_enemy == "mushroom":
                        self.enemy_to_spawn_l.append(MushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "big_mushroom":
                        self.enemy_to_spawn_l.append(BigMushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "flying_eye":
                        self.enemy_to_spawn_l.append(FlyingEyeEnemy(self.sys, pos_, 1))

                    # self.total_enemy += 1

                    self.spw_mul_l -= MULTT
                    self.spw_mul_r += MULTT

            elif self.current_lv == 4:
                random_enemy = random.randint(LOWEST_SPAWN, HIGHT_SPAWN)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    this_enemy = random.choice(lv4_sts['enemy'])
                    if spawn_dir == 0:
                        pos_ = -300 + self.spw_mul_l
                    else:
                        pos_ = self.sys.w+120 + self.spw_mul_r

                    if this_enemy == "skeleton":
                        self.enemy_to_spawn_l.append(SkeletonEnemy(self.sys, pos_, 1))
                    elif this_enemy == "goblin":
                        self.enemy_to_spawn_l.append(GoblinEnemy(self.sys, pos_, 1))
                    elif this_enemy == "mushroom":
                        self.enemy_to_spawn_l.append(MushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "big_mushroom":
                        self.enemy_to_spawn_l.append(BigMushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "flying_eye":
                        self.enemy_to_spawn_l.append(FlyingEyeEnemy(self.sys, pos_, 1))

                    # self.total_enemy += 1

                    self.spw_mul_l -= MULTT
                    self.spw_mul_r += MULTT

            elif self.current_lv == 5:
                random_enemy = random.randint(LOWEST_SPAWN, HIGHT_SPAWN)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    this_enemy = random.choice(lv5_sts['enemy'])
                    if spawn_dir == 0:
                        pos_ = -300 + self.spw_mul_l
                    else:
                        pos_ = self.sys.w+120 + self.spw_mul_r

                    if this_enemy == "skeleton":
                        self.enemy_to_spawn_l.append(SkeletonEnemy(self.sys, pos_, 1))
                    elif this_enemy == "goblin":
                        self.enemy_to_spawn_l.append(GoblinEnemy(self.sys, pos_, 1))
                    elif this_enemy == "mushroom":
                        self.enemy_to_spawn_l.append(MushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "big_mushroom":
                        self.enemy_to_spawn_l.append(BigMushroomEnemy(self.sys, pos_, 1))
                    elif this_enemy == "flying_eye":
                        self.enemy_to_spawn_l.append(FlyingEyeEnemy(self.sys, pos_, 1))

                    # self.total_enemy += 1

                    self.spw_mul_l -= MULTT
                    self.spw_mul_r += MULTT

            self.spw_mul_l = 0
            self.spw_mul_r = 0
        except ValueError:
            print("Error occur while gennerating stage enemy -----------")

    def gennerate_boss(self):
        try:
            if self.current_lv == 1:
                spawn_dir = random.randint(0, 1) # 0 left 1 right
                this_boss = random.choice(lv1_sts['boss'])
                if spawn_dir == 0:
                    pos_ = -460
                else:
                    pos_ = self.sys.w+120

                # print(this_boss)

                if this_boss == "minotaur":
                    self.level_boss.append(MinotaurEnemy(self.sys, pos_, 1))
                elif this_boss == "golem":
                    self.level_boss.append(GolemEnemy(self.sys, pos_, 1))
                elif this_boss == "widow":
                    self.level_boss.append(TarnishedWidowEnemy(self.sys, pos_, 1))

            elif self.current_lv == 2:
                spawn_dir = random.randint(0, 1) # 0 left 1 right
                this_boss = random.choice(lv2_sts['boss'])
                if spawn_dir == 0:
                    pos_ = -460
                else:
                    pos_ = self.sys.w+120

                if this_boss == "minotaur":
                    self.level_boss.append(MinotaurEnemy(self.sys, pos_, 1))
                elif this_boss == "golem":
                    self.level_boss.append(GolemEnemy(self.sys, pos_, 1))
                elif this_boss == "widow":
                    self.level_boss.append(TarnishedWidowEnemy(self.sys, pos_, 1))

            elif self.current_lv == 3:
                spawn_dir = random.randint(0, 1) # 0 left 1 right
                this_boss = random.choice(lv3_sts['boss'])
                if spawn_dir == 0:
                    pos_ = -460
                else:
                    pos_ = self.sys.w+120

                if this_boss == "minotaur":
                    self.level_boss.append(MinotaurEnemy(self.sys, pos_, 1))
                elif this_boss == "golem":
                    self.level_boss.append(GolemEnemy(self.sys, pos_, 1))
                elif this_boss == "widow":
                    self.level_boss.append(TarnishedWidowEnemy(self.sys, pos_, 1))

            elif self.current_lv == 4:
                spawn_dir = random.randint(0, 1) # 0 left 1 right
                this_boss = random.choice(lv4_sts['boss'])
                if spawn_dir == 0:
                    pos_ = -460
                else:
                    pos_ = self.sys.w+120

                if this_boss == "minotaur":
                    self.level_boss.append(MinotaurEnemy(self.sys, pos_, 1))
                elif this_boss == "golem":
                    self.level_boss.append(GolemEnemy(self.sys, pos_, 1))
                elif this_boss == "widow":
                    self.level_boss.append(TarnishedWidowEnemy(self.sys, pos_, 1))

            elif self.current_lv == 5:
                spawn_dir = random.randint(0, 1) # 0 left 1 right
                this_boss = random.choice(lv5_sts['boss'])
                if spawn_dir == 0:
                    pos_ = -460
                else:
                    pos_ = self.sys.w+120

                if this_boss == "minotaur":
                    self.level_boss.append(MinotaurEnemy(self.sys, pos_, 1))
                elif this_boss == "golem":
                    self.level_boss.append(GolemEnemy(self.sys, pos_, 1))
                elif this_boss == "widow":
                    self.level_boss.append(TarnishedWidowEnemy(self.sys, pos_, 1))

        except ValueError:
            print("Error occur while gennerating stage booss -----------")

    def level_selected(self):
        if self.bg == None:
            if self.current_lv == 1:
                self.bg = Background("stage", "s1").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg1.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
            elif self.current_lv == 2:
                self.bg = Background("stage", "s2").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg2.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
            elif self.current_lv == 3:
                self.bg = Background("stage", "s3").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg3.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
            elif self.current_lv == 4:
                self.bg = Background("stage", "s4").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg4.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
            elif self.current_lv == 5:
                self.bg = Background("stage", "s5").get_bg()
                # if self.ambient == None:
                #     self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg5.mp3")).play(loops=-1)
                #     self.ambient.set_volume(1.0)
        self.bg = pygame.transform.scale_by(self.bg, 1.1)

    def check_attack_collide_enemy(self, player_):
        for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
            for j in i:
                if player_.attack_box.colliderect(j.hitbox) and not j.is_hitted:
                    j.is_hitted = True
                    j.health -= (player_.power + self.apply_critical(player_)) # decrease health --------------------
                    self.hit_sound.play()
                    # print(j.health)
                elif not player_.attack_box.colliderect(j.hitbox):
                    j.is_hitted = False

    def check_attack_collide_boss(self, player_):
        for i in self.level_boss:
            if player_.attack_box.colliderect(i.hitbox) and not i.is_hitted:
                i.is_hitted = True
                i.health -= (player_.power + self.apply_critical(player_)) # decrease health --------------------
                self.hit_sound.play()
                # print(j.health)
            elif not player_.attack_box.colliderect(i.hitbox):
                i.is_hitted = False

    def apply_critical(self, player_) -> float:
        if player_.is_comboing:
            ran_ = random.random()
            if ran_ <= player_.critical+0.4:
                # print("PLAYER CRITICALLL")
                return player_.power
            else:
                return 0    
        else:
            ran_ = random.random()
            if ran_ <= player_.critical:
                return player_.power
            else:
                return 0
            
    def apply_critical_enemy(self, enemy_) -> float:
            ran_ = random.random()
            if ran_ <= enemy_.critical_chance+0.2:
                # print("ENEMY CRITICALLL")
                return enemy_.power
            else:
                return 0    
            
    def check_enemy_attack_collide_player(self, player_):
        currently_colliding = set()
        for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
            for j in i:
                if j.attack_box.colliderect(player_.hitbox) and not player_.is_dashing:
                    currently_colliding.add(id(j))
                    if id(j) not in self.enemies_hit_player:
                        player_.health -= (j.power + self.apply_critical_enemy(j))
                        self.enemies_hit_player.add(id(j))
        self.enemies_hit_player = self.enemies_hit_player & currently_colliding # remain the colliding rect, remove old

    def apply_critical_boss(self, boss_) -> float:
            ran_ = random.random()
            if ran_ <= boss_.critical_chance+0.2:
                # print("BOSS CRITICALLL")
                return boss_.power
            else:
                return 0  

    def check_boss_attack_collide_player(self, player_):
        currently_colliding = set()
        for i in self.level_boss:
            if i.attack_box.colliderect(player_.hitbox) and not player_.is_dashing:
                currently_colliding.add(id(i))
                if id(i) not in self.boss_hit_player:
                    player_.health -= (i.power + self.apply_critical_boss(i))
                    self.boss_hit_player.add(id(i))
        self.boss_hit_player = self.boss_hit_player & currently_colliding # remain the colliding rect, remove old

    def show_hitboxes(self, player_):
        if not player_.is_dead:
            pygame.draw.rect(self.screen, (255, 0, 0), player_.hitbox, 5) # hitbox debugging
            pygame.draw.rect(self.screen, (255, 0, 0), player_.attack_box, 5) # attack hitbox debugging

            for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
                for j in i:
                    pygame.draw.rect(self.screen, (255, 0, 0), j.hitbox, 5) # enemy hitbox debugging
                    pygame.draw.rect(self.screen, (0, 0 ,255), j.attack_box, 5) # enemy attack box debugging
            
            if self.level_boss != []:
                for i in self.level_boss:
                    pygame.draw.rect(self.screen, (255, 0, 0), i.hitbox, 5) # boss hitbox debugging
                    pygame.draw.rect(self.screen, (0, 0 ,255), i.attack_box, 5) # boss attack box debugging

    def pause(self, player_):
        cover = pygame.Surface((self.sys.w, self.sys.h), pygame.SRCALPHA)
        cover.fill((0, 0, 0, 120))

        pause_surf = pygame.Surface((700, 200), pygame.SRCALPHA)  # wider box
        pause_surf.fill((0, 0, 0, 180))
        pause_x = self.sys.w // 2 - 350
        pause_y = self.sys.h // 2 - 100

        resume_bt = Button(pause_x + 150, pause_y + 40, 200, 50, "Resume", 24)
        quit_bt = Button(pause_x + 150, pause_y + 100, 200, 50, "Quit", 24)

        # font = pygame.font.Font("./font/Pixelcastle-Regular.otf", 20)
        font = pygame.font.Font(None, 20)

        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        paused = False
                if resume_bt.is_clicked(event):
                    paused = False
                if quit_bt.is_clicked(event):
                    return "quit"

            self.screen.blit(cover, (0, 0))
            self.screen.blit(pause_surf, (pause_x, pause_y))
            resume_bt.create(self.screen)
            quit_bt.create(self.screen)

            stats_x = pause_x + 390
            ememy_killed_surf = font.render(f"Enemies Killed : {self.enemy_killed}", True, (255, 255, 255))
            points_earned_surf = font.render(f"Points Earned  : {self.point_earned}", True, (255, 255, 255))
            self.screen.blit(ememy_killed_surf, (stats_x, pause_y + 65))
            self.screen.blit(points_earned_surf, (stats_x, pause_y + 110))

            pygame.display.flip()
        return "resume"
    
    def show_result(self, player_, is_defeated):
        cover = pygame.Surface((self.sys.w, self.sys.h), pygame.SRCALPHA)
        cover.fill((0, 0, 0, 200))

        result_surf = pygame.Surface((600, 300), pygame.SRCALPHA)
        result_surf.fill((0, 0, 0, 220))
        result_x = self.sys.w // 2 - 300
        result_y = self.sys.h // 2 - 150

        continue_bt = Button(result_x + 200, result_y + 250, 200, 50, "Continue", 24)
        font = pygame.font.Font(None, 30)
        font_title = pygame.font.Font(None, 45)

        showing = True
        while showing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if continue_bt.is_clicked(event):
                    return "continue"

            self.screen.blit(cover, (0, 0))
            self.screen.blit(result_surf, (result_x, result_y))

            if is_defeated == False:
                title = font_title.render("Stage Clear !", True, (255, 220, 50))
                self.screen.blit(title, (result_x + 205, result_y + 30))
            else:
                title = font_title.render("Level Failed !", True, (200, 0, 0))
                self.screen.blit(title, (result_x + 205, result_y + 30))

            killed = font.render(f"Enemies Killed : {self.enemy_killed}", True, (255, 255, 255))
            points = font.render(f"Points Earned  : {self.point_earned}", True, (255, 255, 255))
            health = font.render(f"Health Remaining : {max(0, player_.health)} / {player['health']}", True, (255, 255, 255))

            self.screen.blit(killed, (result_x + 600 // 2 - killed.get_width() // 2, result_y + 110))
            self.screen.blit(points, (result_x + 600 // 2 - points.get_width() // 2, result_y + 150))
            self.screen.blit(health, (result_x + 600 // 2 - health.get_width() // 2, result_y + 190))

            continue_bt.create(self.screen)
            pygame.display.flip()
        return "continue"