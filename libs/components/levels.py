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

class Level:
    def __init__(self, sys, screen, current_lv):
        self.sys = sys
        self.screen = screen
        self.current_lv = current_lv
    
    def show(self):
        if self.current_lv == 1:
            bg = Background("stage", "s1").get_bg()
        elif self.current_lv == 2:
            bg = Background("stage", "s2").get_bg()
        elif self.current_lv == 3:
            bg = Background("stage", "s3").get_bg()
        elif self.current_lv == 4:
            bg = Background("stage", "s4").get_bg()
        elif self.current_lv == 5:
            bg = Background("stage", "s5").get_bg()
            
        bg = pygame.transform.scale_by(bg, 1.1)
        player = Player(self.sys)

        running = True
        while running:
            dashing = False
            jump = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        
                    if event.key == K_SPACE or event.key == K_w:
                        print("jumping")
                        jump = True
                    elif event.key == K_LSHIFT:
                        print("dashing")
                        dashing = True
                        
                elif event.type == QUIT:
                    running = False
                    
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys, dashing, jump)
            
            self.screen.blit(bg, (0, 0))
            self.screen.blit(player.surf, player.rect)
            
            pygame.display.flip()
            