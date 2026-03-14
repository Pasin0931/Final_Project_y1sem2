import pygame
import time

from libs.system_lib import System, Background
from libs.components.ui import Button
from libs.sprites.player import Player

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
        
        self.ambient = None
        self.bg = None
    
    def show(self):
        if self.bg == None:
            if self.current_lv == 1:
                self.bg = Background("stage", "s1").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg1.mp3")).play()
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 2:
                self.bg = Background("stage", "s2").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg2.mp3")).play()
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 3:
                self.bg = Background("stage", "s3").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg3.mp3")).play()
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 4:
                self.bg = Background("stage", "s4").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg4.mp3")).play()
                    self.ambient.set_volume(1.0)
            elif self.current_lv == 5:
                self.bg = Background("stage", "s5").get_bg()
                if self.ambient == None:
                    self.ambient = pygame.mixer.Sound(("./sounds/ambients/stg5.mp3")).play()
                    self.ambient.set_volume(1.0)
            
        self.bg = pygame.transform.scale_by(self.bg, 1.1)
        player = Player(self.sys)

        clock = pygame.time.Clock()

        running = True
        while running:
            dashing = False
            jump = False
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.ambient.stop()
                        self.ambient = None
                        running = False
                        
                    if event.key == K_SPACE or event.key == K_w:
                        # print("jumping")
                        jump = True
                    elif event.key == K_LSHIFT:
                        # print("dashing")
                        dashing = True
                        
                elif event.type == QUIT:
                    self.ambient.stop()
                    self.ambient = None
                    running = False
                    
            pressed_keys = pygame.key.get_pressed()
            player.update(pressed_keys, dashing, jump)
            
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(player.surf, player.rect)

            clock.tick(60)
            
            pygame.display.flip()
            