import pygame
import time

from libs.system_lib import System, Background
from libs.components.ui import Button
from libs.components.levels import Level

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
    def __init__(self, sys, screen, ambient):
        self.sys = sys
        self.screen = screen
        self.ambient = ambient
    
    def show(self):
        
        bg = Background("menu", "selection").get_bg()
        bg = pygame.transform.scale_by(bg, 1.1)
        
        back_b = Button(12, 710, 190, 60, "BacK", 42)
        
        lv1 = Button(290, 410, 70, 70, "l", 50)
        lv2 = Button(528, 410, 70, 70, "ll", 50)
        lv3 = Button(765, 410, 70, 70, "lll", 50)
        lv4 = Button(1000, 410, 70, 70, "lV", 50)
        lv5 = Button(1235, 410, 70, 70, "V", 50)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                elif event.type == QUIT:
                    running = False
                    
                if lv1.is_clicked(event):
                    self.ambient.stop()
                    Level(self.sys, self.screen, 1).show()
                    self.ambient.play()
                elif lv2.is_clicked(event):
                    self.ambient.stop()
                    Level(self.sys, self.screen, 2).show()
                    self.ambient.play()
                elif lv3.is_clicked(event):
                    self.ambient.stop()
                    Level(self.sys, self.screen, 3).show()
                    self.ambient.play()
                elif lv4.is_clicked(event):
                    self.ambient.stop()
                    Level(self.sys, self.screen, 4).show()
                    self.ambient.play()
                elif lv5.is_clicked(event):
                    self.ambient.stop()
                    Level(self.sys, self.screen, 5).show()
                    self.ambient.play()
                
                if back_b.is_clicked(event):
                    running = False

            self.screen.blit(bg, (0, 0))
            
            lv1.create(self.screen)
            lv2.create(self.screen)
            lv3.create(self.screen)
            lv4.create(self.screen)
            lv5.create(self.screen)
            
            back_b.create(self.screen)
            
            pygame.display.flip()