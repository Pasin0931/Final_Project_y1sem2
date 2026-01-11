import pygame
import time

from libs.system_lib import System, Background
from libs.components.ui import Button
from libs.components.level_selection import Selection
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

class main_menu:
    def __init__(self, sys, screen, status):
        self.sys = sys
        self.screen = screen
        self.status = status
    
    def show(self):
        bg = Background("menu", "image").get_bg()
        bg = pygame.transform.scale_by(bg, 1.1) # scale bg image up by 1.1
        # screen.blit(bg, (0, 0))

        play_b = Button(150, 330, 100, 60, "Play", 32)
        control_b = Button(148, 430, 140, 60, "Control", 32)
        summary_b = Button(140, 530, 190, 60, "Summary", 32)
        quit_b = Button(150, 630, 100, 60, "Quit", 32)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        # self.sys.stop()
                
                if play_b.is_clicked(event):
                    print("play")
                    self.status = "play"
                    Selection(self.sys, self.screen).show()
                    
                if control_b.is_clicked(event):
                    print("control")
                    self.status = "control"
                    
                if summary_b.is_clicked(event):
                    print("summary")
                    self.status = "summary"
                    
                if quit_b.is_clicked(event):
                    print("quit")
                    self.status = "quit"
                    running = False
                    
                if event.type == QUIT:
                    running = False
                    
            # screen.fill((0, 0, 0))
            self.screen.blit(bg, (0, 0))
            
            self.sys.paragraph(80, 200, 100, 100, "DarK Impact", (255, 255, 255), 80)
            
            play_b.create(self.screen)
            control_b.create(self.screen)
            summary_b.create(self.screen)
            quit_b.create(self.screen)

            pygame.display.flip()