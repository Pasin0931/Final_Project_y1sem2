import pygame
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

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, sys):
        super(Player, self).__init__()
        self.sys = sys
        
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
        
        self.surf = pygame.image.load("./pictures/player/mc.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        
        self.rect = self.surf.get_rect()
        
        self.rect.x = sys.w // 2.2
        self.rect.y = sys.h // 1.27
        
        self.ground_location = sys.h / 1.27
        
        # -------------jump
        self.jump_h = 2.5
        self.velo = self.jump_h
        self.g = 0.04
        self.on_ground = True
        self.jumping = False
        # -------------
        
        self.is_dashing = False
        self.dash_target = 0
        self.dash_length = 150
        self.dash_speed = 1
        self.facing_L = False
        self.facing_R = False
        
        self.is_moving = False
        # print(self.rect.x, self.rect.y)
        
    def update(self, pressed_keys, dashing, jump):
        # print(self.rect) # debug
        self.is_moving = False
        
        # ---------- Jump
        if (pressed_keys[K_w] or pressed_keys[K_SPACE]) and self.on_ground and jump == True:
            self.velo = self.jump_h
            self.on_ground = False
            self.jumping = True
            
        if not self.on_ground and self.jumping:
            if self.facing_L and not self.facing_R:
                self.surf = pygame.image.load("./pictures/player/anims/jumpl.png").convert_alpha()
            elif not self.facing_L and self.facing_R:
                self.surf = pygame.image.load("./pictures/player/anims/jumpr.png").convert_alpha()
        # ---------- Jump
        
        if pressed_keys[K_a]:
            self.is_moving = True
            if not self.jumping:
                self.surf = pygame.image.load("./pictures/player/anims/runl.png").convert_alpha()
            
            self.facing_L = True
            self.facing_R = False
            self.rect.move_ip(-1, 0) # speed left
        elif pressed_keys[K_d]:
            self.is_moving = True
            if not self.jumping:
                self.surf = pygame.image.load("./pictures/player/anims/runr.png").convert_alpha()
            self.facing_L = False
            self.facing_R = True
            self.rect.move_ip(1, 0) # speed right
        elif pressed_keys[K_s]:
            self.is_moving = False
            self.facing_R = False
            self.facing_L = False
            self.surf = pygame.image.load("./pictures/player/mc.png").convert_alpha()
        
        if self.is_moving == False:   
            if self.facing_L and not self.facing_R:
                self.surf = pygame.image.load("./pictures/player/anims/facel.png").convert_alpha()
            elif not self.facing_L and self.facing_R:
                self.surf = pygame.image.load("./pictures/player/anims/facer.png").convert_alpha()
            
        # ---------- dash     
        if dashing and not self.is_dashing:
            self.is_dashing = True
            if self.facing_L:
                self.dash_target = self.rect.x - self.dash_length
            else:
                self.dash_target = self.rect.x + self.dash_length     
                  
        if self.is_dashing:
            if self.facing_L:
                self.surf = pygame.image.load("./pictures/player/anims/roll_l.png").convert_alpha()
                self.rect.x -= self.dash_speed
                if self.rect.x <= self.dash_target:
                    self.rect.x = self.dash_target
                    self.is_dashing = False
            else:
                self.surf = pygame.image.load("./pictures/player/anims/roll_r.png").convert_alpha()
                self.rect.x += self.dash_speed
                if self.rect.x >= self.dash_target:
                    self.rect.x = self.dash_target
                    self.is_dashing = False
        # ---------- dash  
        
        self.rect.y -= self.velo # -- gravity
        self.velo -= self.g # -- gravity

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.sys.w:
            self.rect.right = self.sys.w
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.ground_location:
            self.rect.bottom = self.ground_location
            self.jumping = False
            self.velo = 0
            self.on_ground = True
            
class attack:
    def __init__(self, player):
        self.player = player