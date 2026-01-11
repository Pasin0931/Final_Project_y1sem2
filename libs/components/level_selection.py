import pygame
import time

from libs.system_lib import System, Background
from libs.components.ui import Button
from libs.sprite_lib import Player

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
)

class Selection:
    def __init__(self, sys, screen):
        self.sys = sys
        self.screen = screen
    
    def show(self):
        bg = Background("menu", "selection").get_bg()
        bg = pygame.transform.scale_by(bg, 1.1)
        
        back_b = Button(12, 710, 190, 60, "BacK", 42)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                elif event.type == QUIT:
                    running = False
                
                if back_b.is_clicked(event):
                    running = False

            self.screen.blit(bg, (0, 0))
            
            back_b.create(self.screen)
            
            pygame.display.flip()