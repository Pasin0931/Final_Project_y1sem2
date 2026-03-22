import pygame
import time

from libs.sprites.sprites_loader_enemy import Skeleton, Goblin, Mushroom, FlyingEye

from ..stat import skeleton, goblin, mushroom, flying_eye, big_mushroom

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sys, spawn_x, speed):
        super(Enemy, self).__init__()
        self.sys = sys
        self.spawn_x = spawn_x
        self.speed = speed

        self.ch_attack_pos = None

        self.health = 8
        self.power = 10
        self.critical_chance = 0.01

        self.is_alive = True
        self.is_hitted = False

        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.rect.x = self.spawn_x
        self.rect.y = sys.h // 1.3 - self.rect.height
        # self.ground_location = sys.h / 1.3
        
        self.is_attacking = False

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.attack_timer = 0
        self.attack_delay = 120  # frames

        self.is_facing_right = True
        self.is_facing_left = False

        self.complete_dead_animation = False
        self.play_attack_animation = False

        self.frame_delay = 6
        self.frame_timer = 0

        self.kill_counted = False

        self.landing_box = [pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)]

    def update(self, player_pos_center, player_is_dead):
        if not self.is_dead():
            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.rect.centerx < player_pos_center-50:
                    if not player_is_dead:
                        self.rect.x += self.speed
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.rect.centerx > player_pos_center+110:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.attack(player_pos_center)

                self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50) # update hitbox
        else:
            self.complete_dead_animation = True

    def attack(self, player_pos):
        self.attack_timer = self.attack_delay  # add this
        if player_pos > self.rect.x + 30:
            # print("attack")
            self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y, 140, 50)
            self.rect.x += 0
        elif player_pos < self.rect.x - 60:
            # print("attack")
            self.attack_box = pygame.Rect(self.hitbox.right-140, self.hitbox.y, 140, 50)
            self.rect.x += 0
        else:
            self.attack_box = pygame.Rect(0, 0, 0, 0)

    def is_dead(self):
        if self.health <= 0:
            self.is_alive = False
            self.attack_box = pygame.Rect(0, 0, 0, 0)
            return True
        return False
    
    def face_left(self):
        if not self.is_facing_left:
            self.is_facing_left = True
            self.is_facing_right = False
            self.surf = pygame.transform.flip(self.surf, True, False)

    def face_right(self):
        if not self.is_facing_right:
            self.is_facing_left = False
            self.is_facing_right = True
            self.surf = pygame.transform.flip(self.surf, True, False)
        
    def frame_progression(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.surf = self.frames[self.frame_index]
            if self.is_facing_left:
                self.surf = pygame.transform.flip(self.surf, True, False)
            
    def set_state(self, state):
        if self.enemy.enemy_state != state:
            self.enemy.enemy_state = state
            self.frames = self.enemy.get_sprite_set()
            self.frames = [pygame.transform.scale_by(f, 2.2) for f in self.frames]
            self.frame_index = 0

    def attack_w_frames(self, player_pos, attack_frame_):
        self.set_state(2)
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

        if self.frame_index == len(self.frames) - 1:
            # print("attack end")
            self.is_attacking = False

    def attack_w_frames_boss(self, player_pos, attack_frame_, state_, w_at, h_at, offset_):
        self.set_state(state_)
        # print(self.frame_index)

        # for minotaur only --------------
        if state_ == 5:
            attack_frame_ = [3, 4, 5, 8, 9, 10, 15, 16, 17, 21, 22, 23, 28, 29, 30, 34, 35, 36, 41, 42, 43, 47, 48, 49]
        #---------------------------------

        if self.frame_index in attack_frame_:
            if player_pos > self.hitbox.centerx:
                # print("attack")
                if self.is_facing_left:
                    self.is_facing_left = False
                    self.is_facing_right = True
                    self.surf = pygame.transform.flip(self.surf, True, False)
                self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y, w_at, h_at)
                self.rect.x += 0
            elif player_pos < self.hitbox.centerx:
                # print("attack")
                if self.is_facing_right:
                    self.is_facing_right = False
                    self.is_facing_left = True
                    self.surf = pygame.transform.flip(self.surf, True, False)
                self.attack_box = pygame.Rect(self.hitbox.left-offset_, self.hitbox.y, w_at, h_at)
                self.rect.x += 0
        else:
            self.attack_box = pygame.Rect(0, 0, 0, 0)

        if self.frame_index == len(self.frames) - 1:
            # print("attack end")
            self.is_attacking = False
            self.ch_attack_pos = None

    def attack_w_frames_boss_golem(self, player_pos, attack_frame_, state_, w_at, h_at, offset_):
        self.set_state(state_)
        # print(self.frame_index)

        if self.frame_index in attack_frame_:
            if player_pos > self.hitbox.centerx:
                # print("attack")
                if self.is_facing_right:
                    self.is_facing_left = True
                    self.is_facing_right = False
                    self.surf = pygame.transform.flip(self.surf, True, False)
                if state_ == 0:
                    self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y + 80, w_at, h_at)
                elif state_ == 1:
                    self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y + 160, 310, 20)
                self.rect.x += 0
            elif player_pos < self.hitbox.centerx:
                # print("attack")
                if self.is_facing_left:
                    self.is_facing_right = True
                    self.is_facing_left = False
                    self.surf = pygame.transform.flip(self.surf, True, False)
                if state_ == 0:
                    self.attack_box = pygame.Rect(self.hitbox.left-offset_, self.hitbox.y + 80, w_at, h_at)
                elif state_ == 1:
                    self.attack_box = pygame.Rect(self.hitbox.left-offset_, self.hitbox.y + 160, 310, 20)
                self.rect.x += 0
        else:
            self.attack_box = pygame.Rect(0, 0, 0, 0)

        if self.frame_index == len(self.frames) - 1:
            # print("attack end")
            self.is_attacking = False
            self.ch_attack_pos = None

    def attack_w_frames_boss_widow(self, player_pos, attack_frame_, state_, w_at, h_at, offset_):
        self.set_state(state_)
        # print(self.frame_index)

        if state_ == 2:
            if self.frame_index in [7, 8, 9]:
                self.landing_box = [
                    pygame.Rect(player_pos-5, self.rect.y+70, 10, 50),  # line
                    pygame.Rect(player_pos-5, self.rect.y+130, 10, 10)  # dot
                ]
            else:
                self.landing_box = [pygame.Rect(0, 0, 0, 0), pygame.Rect(0, 0, 0, 0)]
            if self.frame_index in attack_frame_:
                self.attack_box = pygame.Rect(self.hitbox.left-50, self.hitbox.y+100, 270, 100)
            else:
                self.attack_box = pygame.Rect(0, 0, 0, 0)
        # -----------------------------------

        if self.frame_index in attack_frame_:
            if player_pos > self.hitbox.centerx:
                # print("attack")
                if self.is_facing_left:
                    self.is_facing_left = False
                    self.is_facing_right = True
                    self.surf = pygame.transform.flip(self.surf, True, False)
                if state_ == 0:
                    self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y + 80, w_at, h_at)
                elif state_ == 1:
                    self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y + 130, 350, 20)
                self.rect.x += 0
            elif player_pos < self.hitbox.centerx:
                # print("attack")
                if self.is_facing_right:
                    self.is_facing_right = False
                    self.is_facing_left = True
                    self.surf = pygame.transform.flip(self.surf, True, False)
                if state_ == 0:
                    self.attack_box = pygame.Rect(self.hitbox.left-offset_, self.hitbox.y + 80, w_at, h_at)
                elif state_ == 1:
                    self.attack_box = pygame.Rect(self.hitbox.left-offset_, self.hitbox.y + 130, 350, 20)
                self.rect.x += 0
        else:
            self.attack_box = pygame.Rect(0, 0, 0, 0)

        if self.frame_index == len(self.frames) - 1:
            # print("attack end")
            self.is_attacking = False
            self.ch_attack_pos = None
            self.random_phase = 0
            self.random_phase_rolled = False
            self.is_doing_special_attack = False

class SkeletonEnemy(Enemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.health = skeleton['health']
        self.power = skeleton['power']
        # self.power = 0
        self.critical_chance = skeleton['critical']

        # -------------------------------------        
        self.enemy = Skeleton(0)
        self.frames = self.enemy.get_sprite_set()
        # self.frames = [pygame.transform.scale_by(f, 2.2) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 2.2

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.hitbox.centerx < player_pos_center-150 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x += self.speed
                        self.set_state(1)
                        self.face_right()
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.hitbox.centerx > player_pos_center+150 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                        self.set_state(1)
                        self.face_left()    
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.is_attacking = True

                if self.is_attacking:
                    self.attack_w_frames(player_pos_center, [7, 8])
                
                self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90) # update hitbox

        elif self.health <= 0:
            # print("dead")
            self.set_state(3)
            self.frame_progression()
            if self.frame_index == len(self.frames) - 1:
                self.complete_dead_animation = True


class GoblinEnemy(Enemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.health = goblin['health']
        self.power = goblin['power']
        # self.power = 0
        self.critical_chance = goblin['critical']

        # -------------------------------------        
        self.enemy = Goblin(0)
        self.frames = self.enemy.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 2.18) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 1.89 - self.rect.height

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.hitbox.centerx < player_pos_center-110 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x += self.speed
                        self.set_state(1)
                        self.face_right()
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.hitbox.centerx > player_pos_center+110 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                        self.set_state(1)
                        self.face_left()    
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.is_attacking = True

                if self.is_attacking:
                    self.attack_w_frames(player_pos_center, [9, 10])
                
                self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90) # update hitbox

        elif self.health <= 0:
            # print("dead")
            self.set_state(3)
            self.frame_progression()
            if self.frame_index == len(self.frames) - 1:
                self.complete_dead_animation = True


class MushroomEnemy(Enemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.health = mushroom['health']
        self.power = mushroom['power']
        # self.power = 0
        self.critical_chance = mushroom['critical']

        # -------------------------------------        
        self.enemy = Mushroom(0)
        self.frames = self.enemy.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 2.18) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 1.89 - self.rect.height

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.hitbox.centerx < player_pos_center-150 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x += self.speed
                        self.set_state(1)
                        self.face_right()
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.hitbox.centerx > player_pos_center+150 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                        self.set_state(1)
                        self.face_left()    
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.is_attacking = True

                if self.is_attacking:
                    self.attack_w_frames(player_pos_center, [6, 7, 8, 9])
                
                self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90) # update hitbox

        elif self.health <= 0:
            # print("dead")
            self.set_state(3)
            self.frame_progression()
            if self.frame_index == len(self.frames) - 1:
                self.complete_dead_animation = True


class BigMushroomEnemy(MushroomEnemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.health = big_mushroom['health']
        self.power = big_mushroom['power']
        # self.power = 0
        self.critical_chance = big_mushroom['critical']

        # -------------------------------------        
        self.enemy = Mushroom(0)
        self.frames = self.enemy.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 3.25) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+210, self.rect.y+210, 75, 120)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 2.6 - self.rect.height

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.hitbox.centerx < player_pos_center-150 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x += self.speed
                        self.set_state(1)
                        self.face_right()
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.hitbox.centerx > player_pos_center+150 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                        self.set_state(1)
                        self.face_left()    
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.is_attacking = True

                if self.is_attacking:
                    self.attack_w_frames(player_pos_center, [6, 7, 8, 9])
                
                self.hitbox = pygame.Rect(self.rect.x+210, self.rect.y+210, 75, 120) # update hitbox

        elif self.health <= 0:
            # print("dead")
            self.set_state(3)
            self.frame_progression()
            if self.frame_index == len(self.frames) - 1:
                self.complete_dead_animation = True

    def set_state(self, state):
        if self.enemy.enemy_state != state:
            self.enemy.enemy_state = state
            self.frames = self.enemy.get_sprite_set()
            self.frames = [pygame.transform.scale_by(f, 3.25) for f in self.frames]
            self.frame_index = 0


class FlyingEyeEnemy(Enemy):
    def __init__(self, sys, spawn_x, speed):
        super().__init__(sys, spawn_x, speed)

        self.health = flying_eye['health']
        self.power = flying_eye['power']
        # self.power = 0
        self.critical_chance = flying_eye['critical']

        # -------------------------------------        
        self.enemy = FlyingEye(0)
        self.frames = self.enemy.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 2.18) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 

        self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.rect.y = sys.h // 2.1 - self.rect.height

    def update(self, player_pos_center, player_is_dead):
        if self.health > 0 and not player_is_dead:
            self.frame_progression()

            if self.attack_timer > 0: # stop
                self.attack_timer -= 1
            else:
                if self.hitbox.centerx < player_pos_center-60 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x += self.speed
                        self.set_state(0)
                        self.face_right()
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                elif self.hitbox.centerx > player_pos_center+60 and not self.is_attacking:
                    if not player_is_dead:
                        self.rect.x -= self.speed
                        self.set_state(0)
                        self.face_left()    
                    self.attack_box = pygame.Rect(0, 0, 0, 0)
                else:
                    self.is_attacking = True

                if self.is_attacking:
                    self.attack_w_frames(player_pos_center, [7, 8, 9])
                
                self.hitbox = pygame.Rect(self.rect.x+130, self.rect.y+135, 75, 90) # update hitbox

        elif self.health <= 0:
            # print("dead")
            self.set_state(3)
            self.frame_progression()
            if self.rect.y <= 330:
                self.rect.y += 4
            if self.frame_index == len(self.frames) - 1:
                self.complete_dead_animation = True