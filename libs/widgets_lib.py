import pygame

from pygame.locals import (
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

class System:
    def __init__(self, w, h, r, g, b):
        self.w = w
        self.h = h

        self.screen = pygame.display.set_mode([self.w, self.h])
        self.screen.fill((r, g, b)) # bg color

    def get_screen(self):
        return self.screen
    
    def setBg(self, r, g, b):
        self.screen.fill((r, g, b))
        
    def draw_rect(self, r, g, b, x, y, w, h):
        pygame.draw.rect(self.screen, (r, g, b), (x, y, w, h))
        
    def draw_circle(self, r, g, b, x, y, p):
        pygame.draw.circle(self.screen, (r, g, b), (x, y), p)
    
    def initialize(self):
        pygame.init()
        
    def stop(self):
        pygame.quit()
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        
    def update(self, sys, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_a]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(1, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > sys.w:
            self.rect.right = sys.w
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= sys.h:
            self.rect.bottom = sys.h