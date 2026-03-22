import pygame
import time
import random

from libs.system_lib import System, Background
from libs.components.ui import Button, HealthBar, StaminaBar, BossHealthBar
from libs.sprites.player import Player
from libs.sprites.enemy import Enemy, SkeletonEnemy, GoblinEnemy, MushroomEnemy, BigMushroomEnemy, FlyingEyeEnemy
from libs.sprites.boss import MinotaurEnemy, GolemEnemy, TarnishedWidowEnemy

from ..stat import player as player_default_stat, lv1_sts, lv2_sts, lv3_sts, lv4_sts, lv5_sts, minotaur, stone_golem, tarnished_widow

MULTT = 500

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
    MOUSEBUTTONDOWN
)

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
    
    def show(self):
        self.level_selected()

        player_ = Player(self.sys)

        healthbar_ = HealthBar(self.screen, 30, 172, player_default_stat['health'], 20, player_.health)
        staminabar_ = StaminaBar(self.screen, 30, 200, player_default_stat['stamina'], 20, player_.stamina)

        self.gennerate_enemy()
        self.gennerate_boss()
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
                            self.ambient.stop()
                            self.ambient = None
                            running = False
                        
                    if event.key == K_SPACE or event.key == K_w:
                        # print("jumping")
                        jump = True
                    elif event.key == K_LSHIFT:
                        # print("dashing")
                        dashing = True

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        attack_click = True
                    else:
                        combo_click = True
                    # print(attack_click, combo_click)
                        
                elif event.type == QUIT:
                    result = self.pause(player_)
                    if result == "quit":
                        self.ambient.stop()
                        self.ambient = None
                        running = False

            pressed_keys = pygame.key.get_pressed()
            player_.update(pressed_keys, dashing, jump, attack_click, combo_click)
            
            self.screen.blit(self.bg, (0, 0))

            if len(self.enemy_to_spawn_l) + len(self.enemy_to_spawn_r) > 0:
                for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
                    for j in i:
                        j.update(player_.hitbox.centerx, player_.is_dead)
                        self.screen.blit(j.surf, j.rect)
                        if j.health <= 0 and not j.kill_counted:
                            j.kill_counted = True
                            self.enemy_killed += 1

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

                self.check_attack_collide_boss(player_)
                self.check_boss_attack_collide_player(player_)

                self.level_boss = [i for i in self.level_boss if not i.complete_dead_animation]

                for i in self.level_boss:
                    self.sys.paragraph(320, 625, 100, 100, f"{i.boss_name}", (255, 255, 255), 20)
                    boss_healthbar_.update_health(i.health)

            self.show_hitboxes(player_) # hitboxes display
            healthbar_.update_health(player_.health)
            staminabar_.update_stamina(player_.stamina)
            # print(player_.health)

            # self.sys.paragraph_normal(320, 200, 100, 100, f"{len(self.enemy_to_spawn_l)+len(self.enemy_to_spawn_r)}/{self.total_enemy}", (255, 255, 255), 60)
            self.screen.blit(player_.surf, player_.rect)

            clock.tick(60)
            
            pygame.display.flip()
            
    def level_selected(self):
        if self.bg == None:
            if self.current_lv == 1:
                self.bg = Background("stage", "s1").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg1.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 2:
                self.bg = Background("stage", "s2").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg2.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 3:
                self.bg = Background("stage", "s3").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg3.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 4:
                self.bg = Background("stage", "s4").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg4.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 5:
                self.bg = Background("stage", "s5").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg5.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
        self.bg = pygame.transform.scale_by(self.bg, 1.1)

    def gennerate_enemy(self):
        try:
            if self.current_lv == 1:
                random_enemy = random.randint(0, 0)
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
                random_enemy = random.randint(1, 3)
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
                random_enemy = random.randint(1, 3)
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
                random_enemy = random.randint(1, 3)
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
                random_enemy = random.randint(1, 3)
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
                    pos_ = -360
                else:
                    pos_ = self.sys.w+120

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
                    pos_ = -360
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
                    pos_ = -360
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
                    pos_ = -360
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
                    pos_ = -360
                else:
                    pos_ = self.sys.w+120

                if this_boss == "minotaur":
                    self.level_boss.append(MinotaurEnemy(self.sys, pos_, 1))
                elif this_boss == "golem":
                    self.level_boss.append(GolemEnemy(self.sys, pos_, 1))
                elif this_boss == "widow":
                    self.level_boss.append(TarnishedWidowEnemy(self.sys, pos_, 1))

        except ValueError:
            print("Error occur while gennerating stage enemy -----------")

    def level_selected(self):
        if self.bg == None:
            if self.current_lv == 1:
                self.bg = Background("stage", "s1").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg1.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 2:
                self.bg = Background("stage", "s2").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg2.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 3:
                self.bg = Background("stage", "s3").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg3.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 4:
                self.bg = Background("stage", "s4").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg4.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 5:
                self.bg = Background("stage", "s5").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg5.mp3")).play(loops=-1)
                    self.ambient.set_volume(1.0)
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
                print("PLAYER CRITICALLL")
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
                print("ENEMY CRITICALLL")
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
                print("ENEMY CRITICALLL")
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