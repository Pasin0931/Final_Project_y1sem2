import pygame
from .sprites_loader import Knight, FemaleKnight
from ..stat import player
import random
import time

JUMP_STAMINA_DECREASE = 25
DASH_STAMINA_DECREASE = 25
ATTACK_STAMINA_DECREASE = 25
ATTACK2_STAMINA_DECREASE = 50

DASH_SPEED = 3.15

STAMINA_REGEN = 1

FRAME_STAMINA_COOLDOWN = 40

FRAME_ATTACK1_TO_ANIMATE = 20
FRAME_ATTACK2_TO_ANIMATE = 40

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
    K_SPACE,
    K_LSHIFT
)

class Player(pygame.sprite.Sprite):
    def __init__(self, sys):
        super(Player, self).__init__()
        self.sys = sys

        # ------
        self.health = player["health"]
        self.power = player["power"]
        self.critical = player["critical"]
        self.stamina = player["stamina"]
        self.level_point = 0
        # ------

        self.ground_location = sys.h / 1.3

        # -------------------------------------        
        self.knight = Knight(0)
        # self.knight = FemaleKnight(0)
        self.frames = self.knight.get_sprite_set()
        self.frames = [pygame.transform.scale_by(f, 3) for f in self.frames]
        self.frame_index = 0
        self.surf = self.frames[self.frame_index]
        # ------------------------------------- 
        
        self.rect = self.surf.get_rect()

        self.rect.x = sys.w // 2.6 # spawn point
        self.rect.y = sys.h // 1.27

        self.on_ground = True
        self.velo = 0
        self.jump_cooldown = 0
        self.is_jumping = False

        self.is_facing_right = True
        self.is_facing_left = False

        self.is_dashing = False
        self.dash_end_point = 0

        self.frame_timer = 0
        self.frame_delay = 5  # frames wait before next sprite frame

        self.walk_sound = pygame.mixer.Sound("./sounds/player/walking_sound.mp3") # sound -----
        self.walk_sound.set_volume(0.3)
        self.walk_sound_timer = 0
        self.walk_sound_delay = 26  # frames between each play

        self.sword_swing = pygame.mixer.Sound("./sounds/player/sword_swing.mp3") # sword sound -----
        self.sword_swing.set_volume(0.6)
    
        self.roll_ = pygame.mixer.Sound("./sounds/player/roll.mp3") # sword sound -----
        self.roll_.set_volume(0.5)

        self.cool_down_before_stamina_regen = 0

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 60, 115)
        self.hitbox.x = self.rect.x

        self.is_attacking = False
        self.is_comboing = False
        self.frame_attack = 0
        self.frame_combo = 0

        self.attack_box = pygame.Rect(0, 0, 0, 0)

        self.sound_tmp = None

        self.is_dead = False
        self.play_dead_anim = False

    def update(self, pressed_keys, dashing_, jump_, attack_, combo_):
        if not self.is_dead:
            self.velo += 0.5
            self.rect.y += self.velo

            if pressed_keys[K_d] and not self.is_jumping and not self.is_dashing:
                if self.is_attacking or self.is_comboing:
                    self.rect.x += 1
                else:
                    self.set_state(1)
                    self.rect.x += 2
                self.face_right()
                if self.walk_sound_timer <= 0:
                    self.walk_sound.play()
                    self.walk_sound_timer = self.walk_sound_delay
            elif pressed_keys[K_a] and not self.is_jumping and not self.is_dashing:
                if self.is_attacking or self.is_comboing:
                    self.rect.x -= 1
                else:
                    self.set_state(1)
                    self.rect.x -= 2
                self.face_left()
                if self.walk_sound_timer <= 0:
                    self.walk_sound.play()
                    self.walk_sound_timer = self.walk_sound_delay
            elif not self.is_jumping and not self.is_dashing and not self.is_attacking and not self.is_comboing:
                self.set_state(0)  # idle

            if jump_:
                self.jump()

            if self.health <= 0:
                self.is_dead = True

            # --------- Dodge
            if dashing_ and not self.is_dashing and not self.is_attacking and not self.is_jumping and not self.is_comboing:
                # print(self.stamina)
                if self.stamina - DASH_STAMINA_DECREASE >= 0:
                    self.roll_.play()
                    self.is_dashing = True
                    self.set_state(6)  # roll
                    self.check_not_same_bool()
                    self.stamina -= DASH_STAMINA_DECREASE
                    self.cool_down_before_stamina_regen = 0
                    if self.is_facing_left:
                        self.dash_end_point = max(0, self.rect.x - 170)
                    else:
                        self.dash_end_point = min(self.sys.w, self.rect.x + 170)
            # ---------- attack
            if attack_ and not self.is_attacking and not self.is_dashing and not self.is_jumping and not self.is_comboing:
                if self.stamina - ATTACK_STAMINA_DECREASE >= 0:
                    self.is_attacking = True
                    ran_attack_anim = random.randint(2,3)
                    self.set_state(ran_attack_anim)
                    self.check_not_same_bool()
                    self.stamina -= ATTACK_STAMINA_DECREASE
                    self.cool_down_before_stamina_regen = 0
                    self.sword_swing.play()
            # ---------- Combo
            if combo_ and not self.is_comboing and not self.is_dashing and not self.is_jumping and not self.is_attacking:
                if self.stamina - ATTACK2_STAMINA_DECREASE >= 0:
                    self.is_comboing = True
                    self.set_state(4)
                    self.check_not_same_bool()
                    self.stamina -= ATTACK2_STAMINA_DECREASE
                    self.cool_down_before_stamina_regen = 0
            # ----------

            if self.stamina < player["stamina"]:
                if not self.is_dashing and not self.is_jumping and self.on_ground and not self.is_attacking and not self.is_comboing:
                    if self.cool_down_before_stamina_regen < FRAME_STAMINA_COOLDOWN:
                        self.cool_down_before_stamina_regen += 1
                    elif self.cool_down_before_stamina_regen >= FRAME_STAMINA_COOLDOWN:
                        self.stamina+=STAMINA_REGEN
                        if self.stamina >= player['stamina']:
                            self.stamina = player['stamina']
                            self.cool_down_before_stamina_regen = 0

            if self.is_dashing:
                self.dash(self.dash_end_point)

            if self.is_attacking:
                self.attack()
            
            if self.is_comboing:
                self.combo()

            if self.jump_cooldown > 0:
                self.jump_cooldown -= 1

            if self.rect.left <= 0:
                self.rect.left = 0
                self.is_dashing = False
                # self.set_state(0)
            if self.rect.right >= self.sys.w:
                self.rect.right = self.sys.w
                self.is_dashing = False
                # self.set_state(0)
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= self.ground_location:
                self.rect.bottom = self.ground_location
                self.on_ground = True
                self.is_jumping = False

            self.frame_timer += 1 # FRAME PROGRESSIONNNNNNNNNN
            if self.frame_timer >= self.frame_delay:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.surf = self.frames[self.frame_index]
                if self.is_facing_left:
                    self.surf = pygame.transform.flip(self.surf, True, False)

            if self.walk_sound_timer > 0: # sound -------------
                self.walk_sound_timer -= 1

            self.hitbox.midbottom = self.rect.midbottom
            if self.is_facing_right:
                self.hitbox.x -= 14
            else:
                self.hitbox.x += 14
        else:
            if not self.play_dead_anim:
                self.set_state(5)
                self.frame_timer += 1 # FRAME PROGRESSIONNNNNNNNNN
                if self.frame_timer >= self.frame_delay:
                    self.frame_timer = 0
                    self.frame_index = (self.frame_index + 1) % len(self.frames)
                    self.surf = self.frames[self.frame_index]
                    # print(self.frame_index, len(self.frames))
                    if self.is_facing_left:
                        self.surf = pygame.transform.flip(self.surf, True, False)
                    if self.frame_index == len(self.frames) - 1:
                        self.play_dead_anim = True

    def set_state(self, state):
        if self.knight.knight_state != state:
            self.knight.knight_state = state
            self.frames = self.knight.get_sprite_set()
            self.frames = [pygame.transform.scale_by(f, 3) for f in self.frames]
            self.frame_index = 0

    def jump(self):
        if self.on_ground and self.jump_cooldown <= 0:
            if self.stamina - JUMP_STAMINA_DECREASE >= 10:
                self.stamina -= JUMP_STAMINA_DECREASE
                self.cool_down_before_stamina_regen = 0
                self.velo = -6
                self.on_ground = False
                self.jump_cooldown = 30 # frames
                self.is_jumping = True

    def dash(self, end_point):
        if self.is_facing_left:
            if self.rect.x > end_point:
                self.rect.x -= DASH_SPEED - 1
            else:
                self.is_dashing = False
                self.set_state(0)
        else:
            if self.rect.x < end_point:
                self.rect.x += DASH_SPEED
            else:
                self.is_dashing = False
                self.set_state(0)

    def check_not_same_bool(self):
        if self.is_facing_left == self.is_facing_right:
            self.is_facing_right = True
            self.is_facing_left = False

    def face_left(self):
        if not self.is_facing_left and not self.is_attacking and not self.is_comboing:
            self.is_facing_left = True
            self.is_facing_right = False
            self.surf = pygame.transform.flip(self.surf, True, False)

    def face_right(self):
        if not self.is_facing_right and not self.is_attacking and not self.is_comboing:
            self.is_facing_left = False
            self.is_facing_right = True
            self.surf = pygame.transform.flip(self.surf, True, False)

    def attack(self):
        if self.frame_index >= len(self.frames) - 1:
            self.is_attacking = False
            self.frame_attack = 0
            self.attack_box = pygame.Rect(0, 0, 0, 0)
            self.set_state(0)

        if self.is_attacking:
            if self.is_facing_right:
                self.attack_box = pygame.Rect(self.hitbox.right, self.hitbox.y, 92, 115)
            else:
                self.attack_box = pygame.Rect(self.hitbox.left - 92, self.hitbox.y, 92, 115)

    def combo(self):
        if self.frame_index >= len(self.frames) - 1:
            self.is_comboing = False
            self.frame_combo = 0
            self.attack_box = pygame.Rect(0, 0, 0, 0)
            self.sound_tmp = None
            self.set_state(0)

        if self.is_comboing and self.frame_index in [1,2,3,6,7,8]:
            if self.frame_index == 1 and self.sound_tmp == None:
                self.sound_tmp = 1
                self.sword_swing.play()
            elif self.frame_index == 6 and self.sound_tmp == 1:
                self.sword_swing.play()
                self.sound_tmp = 6

            if self.is_facing_right:
                self.attack_box = pygame.Rect(self.hitbox.right, self.hitbox.y, 120, 115)
            else:
                self.attack_box = pygame.Rect(self.hitbox.left - 120, self.hitbox.y, 120, 115) # 123678
        else:
            self.attack_box = pygame.Rect(0, 0, 0, 0)
        # print(self.frame_index)