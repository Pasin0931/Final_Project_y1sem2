import pygame
import time
import random

from libs.system_lib import System, Background
from libs.components.ui import Button, HealthBar, StaminaBar
from libs.sprites.player import Player
from libs.sprites.enemy import Enemy, SkeletonEnemy, GoblinEnemy, MushroomEnemy, BigMushroomEnemy, FlyingEyeEnemy

from ..stat import player as player_default_stat

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

        self.hit_sound = pygame.mixer.Sound(("./sounds/player/flesh_swing.mp3"))
        self.hit_sound.set_volume(0.4)
    
    def show(self):
        self.level_selected()

        player_ = Player(self.sys)

        healthbar_ = HealthBar(self.screen, 30, 172, player_default_stat['health'], 20, player_.health)
        staminabar_ = StaminaBar(self.screen, 30, 200, player_default_stat['stamina'], 20, player_.stamina)

        self.gennerate_enemy()

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
                    self.ambient.stop()
                    self.ambient = None
                    running = False
                    
            pressed_keys = pygame.key.get_pressed()
            player_.update(pressed_keys, dashing, jump, attack_click, combo_click)
            
            
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(player_.surf, player_.rect)

            for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
                for j in i:
                    j.update(player_.hitbox.centerx, player_.is_dead)
                    self.screen.blit(j.surf, j.rect)

            self.show_hitboxes(player_) # hitboxes display

            self.check_attack_collide_enemy(player_)
            self.check_enemy_attack_collide_player(player_)
            self.enemy_to_spawn_l = [i for i in self.enemy_to_spawn_l if i.health > 0]
            self.enemy_to_spawn_r = [i for i in self.enemy_to_spawn_r if i.health > 0]

            healthbar_.update_health(player_.health)
            staminabar_.update_stamina(player_.stamina)

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
                random_enemy = random.randint(1, 4) # 5, 10
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    if spawn_dir == 0:
                        self.enemy_to_spawn_l.append(SkeletonEnemy(self.sys, self.sys.w-40, 1))
                    else:
                        self.enemy_to_spawn_r.append(SkeletonEnemy(self.sys, self.sys.w+40, 1))
            
            elif self.current_lv == 2:
                random_enemy = random.randint(10, 15)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    if spawn_dir == 0:
                        self.enemy_to_spawn_l.append(Enemy(self.sys, -40, 1))
                    else:
                        self.enemy_to_spawn_r.append(Enemy(self.sys, self.sys.w+40, 1))

            elif self.current_lv == 3:
                random_enemy = random.randint(15, 20)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    if spawn_dir == 0:
                        self.enemy_to_spawn_l.append(Enemy(self.sys, -40, 1))
                    else:
                        self.enemy_to_spawn_r.append(Enemy(self.sys, self.sys.w+40, 1))

            elif self.current_lv == 4:
                random_enemy = random.randint(20, 25)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    if spawn_dir == 0:
                        self.enemy_to_spawn_l.append(Enemy(self.sys, -40, 1))
                    else:
                        self.enemy_to_spawn_r.append(Enemy(self.sys, self.sys.w+40, 1))

            elif self.current_lv == 5:
                random_enemy = random.randint(25, 30)
                # print(random_enemy)
                for i in range(random_enemy):
                    spawn_dir = random.randint(0, 1) # 0 left 1 right
                    if spawn_dir == 0:
                        self.enemy_to_spawn_l.append(Enemy(self.sys, -40, 1))
                    else:
                        self.enemy_to_spawn_r.append(Enemy(self.sys, self.sys.w+40, 1))

        except ValueError:
            print("Error occur while gennerating stage enemy -----------")

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

    def apply_critical(self, player_) -> float:
        if player_.is_comboing:
            ran_ = random.random()
            if ran_ <= player_.critical+0.4:
                print("CRITICALLL")
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
                # print("CRITICALLL")
                return enemy_.power
            else:
                return 0    
            
    def check_enemy_attack_collide_player(self, player_):
        collided = False
        for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
            for j in i:
                if j.attack_box.colliderect(player_.hitbox) and not player_.is_dashing:
                    collided = True
                    if player_.collide_with_enemy_attack == False:
                        player_.health -= (j.power + self.apply_critical_enemy(j)) # decrease health player --------------------
                        # print(player_.health)
                        player_.collide_with_enemy_attack = True
                        print("player hurt")
        if not collided:
            player_.collide_with_enemy_attack = False

    def show_hitboxes(self, player_):
        if not player_.is_dead:
            pygame.draw.rect(self.screen, (255, 0, 0), player_.hitbox, 5) # hitbox debugging
            pygame.draw.rect(self.screen, (255, 0, 0), player_.attack_box, 5) # attack hitbox debugging

            for i in [self.enemy_to_spawn_l, self.enemy_to_spawn_r]:
                for j in i:
                    pygame.draw.rect(self.screen, (255, 0, 0), j.hitbox, 5) # enemy hitbox debugging
                    pygame.draw.rect(self.screen, (0, 0 ,255), j.attack_box, 5) # enemy attack box debugging