import pygame
from libs.components.ui import Button

from ..db.playerDb import PlayerStats

from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

class Summary:
    def __init__(self, sys, screen):
        self.sys = sys
        self.screen = screen

    def show(self):

        back_b = Button(40, 635, 150, 60, "BacK", 32)

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == QUIT:
                    running = False

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                if back_b.is_clicked(event):
                    running = False

            self.screen.fill((0, 0, 0))

            back_b.create(self.screen)

            pygame.display.flip()
