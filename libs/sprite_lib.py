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
    K_d
)

class Player(pygame.sprite.Sprite):
    def __init__(self, sys):
        super(Player, self).__init__()
        self.sys = sys
        
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        
        self.surf = pygame.image.load("./pictures/player/mc.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        
        self.rect = self.surf.get_rect()
        
        self.rect.x = sys.w / 2.2
        self.rect.y = sys.h / 2.5
        
        print(self.rect.x, self.rect.y)
        
    def update(self, pressed_keys):
        # print(self.rect) # debug
        
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -1) # speed up
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1) # speed down
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0) # speed left
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0) # speed right

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.sys.w:
            self.rect.right = self.sys.w
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.sys.h:
            self.rect.bottom = self.sys.h