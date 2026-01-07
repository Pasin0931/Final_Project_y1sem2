import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
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