import pygame
import random
from ..name_gennerator import BossNameGennerator
from .enemy import Enemy

from libs.sprites.sprites_loader_boss import Minotaur, Golem, TarnishedWidow

from ..stat import minotaur, stone_golem, tarnished_widow

from ..name_gennerator import BossNameGennerator

class MinotaurEnemy(Enemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.health = minotaur['health']
        self.power = minotaur['power']
        # self.power = 0
        self.critical_chance = minotaur['critical']

        # -------------------------------------        
        self.enemy = Minotaur(3)
        self.frames = self.enemy.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 3) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+210, self.rect.y+210, 75, 120)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 2.8 - self.rect.height

        self.speed = 2.35

        self.boss_name = BossNameGennerator('./libs/listofnames.csv').random_name("minotaur")
        print(self.boss_name)

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.hitbox.centerx < player_pos_center-140:
                    if not player_is_dead:
                        self.rect.x += self.speed
                        self.set_state(4)
                        self.face_right()
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.hitbox.centerx > player_pos_center+140:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                        self.set_state(4)
                        self.face_left()    
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.attack_w_frames_boss(player_pos_center, [3, 4, 5], 0, 200, 100, 125)
                
                if self.is_facing_right:
                    self.hitbox = pygame.Rect(self.rect.x+100, self.rect.y+210, 75, 120) # update hitbox
                else:
                    self.hitbox = pygame.Rect(self.rect.x+210, self.rect.y+210, 75, 120) # update hitbox

        elif self.health <= 0:
            # print("dead")
            self.set_state(2)
            self.frame_progression()
            if self.frame_index == len(self.frames) - 1:
                self.complete_dead_animation = True

    def set_state(self, state):
        if self.enemy.enemy_state != state:
            self.enemy.enemy_state = state
            self.frames = self.enemy.get_sprite_set()
            self.frames = [pygame.transform.scale_by(f, 3) for f in self.frames]
            self.frame_index = 0

    def face_left(self):
        if not self.is_facing_left:
            self.is_facing_left = True
            self.is_facing_right = False
            self.surf = pygame.transform.flip(self.surf, True, False)
            self.rect.x -= 70

    def face_right(self):
        if not self.is_facing_right:
            self.is_facing_left = False
            self.is_facing_right = True
            self.surf = pygame.transform.flip(self.surf, True, False)
            self.rect.x += 70


class GolemEnemy(Enemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.health = stone_golem['health']
        self.power = stone_golem['power']
        # self.power = 0
        self.critical_chance = stone_golem['critical']

        # -------------------------------------        
        self.enemy = Golem(3)
        self.frames = self.enemy.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 3) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+210, self.rect.y+210, 75, 120)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 2.8 - self.rect.height

        self.boss_name = BossNameGennerator('./libs/listofnames.csv').random_name("minotaur")
        print(self.boss_name)

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.hitbox.centerx < player_pos_center-90:
                    if not player_is_dead:
                        self.rect.x += self.speed
                        self.set_state(4)
                        self.face_right()
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.hitbox.centerx > player_pos_center+90:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                        self.set_state(4)
                        self.face_left()    
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.attack_w_frames(player_pos_center, [6, 7, 8, 9])
                
                self.hitbox = pygame.Rect(self.rect.x+210, self.rect.y+210, 75, 120) # update hitbox

        elif self.health <= 0:
            # print("dead")
            self.set_state(2)
            self.frame_progression()
            if self.frame_index == len(self.frames) - 1:
                self.complete_dead_animation = True

    def attack_w_frames(self, player_pos, attack_frame_):
        # random.choice([self.set_state(0), self.set_state(1)])
        self.set_state(0)
        # print(self.frame_index)
        if self.frame_index in attack_frame_:
            if player_pos > self.hitbox.centerx:
                # print("attack")
                if self.is_facing_left:
                    self.is_facing_left = False
                    self.is_facing_right = True
                    self.surf = pygame.transform.flip(self.surf, True, False)
                self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y, 170, 110)
                self.rect.x += 0
            elif player_pos < self.hitbox.centerx:
                # print("attack")
                if self.is_facing_right:
                    self.is_facing_right = False
                    self.is_facing_left = True
                    self.surf = pygame.transform.flip(self.surf, True, False)
                self.attack_box = pygame.Rect(self.hitbox.left-95, self.hitbox.y, 170, 110)
                self.rect.x += 0
        else:
            self.attack_box = pygame.Rect(0, 0, 0, 0)

    def set_state(self, state):
        if self.enemy.enemy_state != state:
            self.enemy.enemy_state = state
            self.frames = self.enemy.get_sprite_set()
            self.frames = [pygame.transform.scale_by(f, 3) for f in self.frames]
            self.frame_index = 0