import pygame
import time

from libs.system_lib import System, Background
from libs.components.ui import Button
from libs.components.level_selection import Selection

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
        sound = pygame.mixer.Sound("./sounds/click.mp3")
        ambient = pygame.mixer.Sound("./sounds/caelid.mp3")
        sound.set_volume(1.0)
        ambient.set_volume(1.0)
        
        ambient.play()
        
        bg = Background("menu", "image").get_bg()
        bg = pygame.transform.scale_by(bg, 1.1) # scale bg image up by 1.1
        # screen.blit(bg, (0, 0))

        play_b = Button(120, 280, 100, 60, "Play", 32)
        setting_b = Button(118, 365, 140, 60, "Setting", 32)
        summary_b = Button(110, 450, 190, 60, "Summary", 32)
        quit_b = Button(120, 530, 100, 60, "Quit", 32)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    self.status = "quit"
                    break
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        # self.sys.stop()
                
                if play_b.is_clicked(event):
                    # print("play")
                    sound.play()
                    self.status = "play"
                    Selection(self.sys, self.screen, ambient).show()
                    
                if setting_b.is_clicked(event):
                    # print("control")
                    sound.play()
                    self.status = "setting"
                    
                if summary_b.is_clicked(event):
                    # print("summary")
                    sound.play()
                    self.status = "summary"
                    
                if quit_b.is_clicked(event):
                    # print("quit")
                    sound.play()
                    self.status = "quit"
                    running = False
                    
                if event.type == QUIT:
                    running = False
                    
            # screen.fill((0, 0, 0))
            self.screen.blit(bg, (0, 0))
            
            self.sys.paragraph(70, 170, 100, 100, "DarK Impact", (255, 255, 255), 65)
            
            play_b.create(self.screen)
            setting_b.create(self.screen)
            summary_b.create(self.screen)
            quit_b.create(self.screen)

            pygame.display.flip()