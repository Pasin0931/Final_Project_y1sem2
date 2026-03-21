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

        self.boss_class = "minotaur"

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

        self.speed = 1

        self.boss_name = BossNameGennerator('./libs/listofnames.csv').random_name("minotaur")
        print(self.boss_name)

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.hitbox.centerx < player_pos_center-140:
                if not player_is_dead and not self.is_attacking:
                    self.rect.x += self.speed
                    self.set_state(4)
                    self.face_right()
                self.attack_box = pygame.Rect(0, 0, 0, 0)
            elif self.hitbox.centerx > player_pos_center+140:
                if not player_is_dead and not self.is_attacking:
                    self.rect.x -= self.speed
                    self.set_state(4)
                    self.face_left()    
                self.attack_box = pygame.Rect(0, 0, 0, 0)
            else:
                if self.ch_attack_pos == None:
                    if self.health >= (minotaur['health'] / 2):
                        self.ch_attack_pos = random.choice([0, 1])
                    else:
                        self.ch_attack_pos = random.choice([0, 1, 5])
                self.is_attacking = True

            if self.is_attacking:
                # print(self.ch_attack_pos, "-----")
                self.attack_w_frames_boss(player_pos_center, [3, 4, 5], self.ch_attack_pos, 200, 100, 125)
            
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

        self.boss_class = "stone_golem"

        self.health = minotaur['health']
        self.power = minotaur['power']
        # self.power = 0
        self.critical_chance = minotaur['critical']

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

        self.speed = 0.8

        self.boss_name = BossNameGennerator('./libs/listofnames.csv').random_name("golem")
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

class TarnishedWidowEnemy(Enemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.boss_class = "tarnished_widow"

        self.health = minotaur['health']
        self.power = minotaur['power']
        # self.power = 0
        self.critical_chance = minotaur['critical']

        # -------------------------------------        
        self.enemy = TarnishedWidow(3)
        self.frames = self.enemy.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 3) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+210, self.rect.y+210, 75, 120)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 2.8 - self.rect.height

        self.speed = 2.35

        self.boss_name = BossNameGennerator('./libs/listofnames.csv').random_name("widow")
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