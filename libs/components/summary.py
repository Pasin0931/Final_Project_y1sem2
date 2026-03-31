import pygame
from libs.components.ui import Button

from ..db.playerDb import PlayerStats
from ..db.plot_func import Plotter

from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

class Summary:
    def __init__(self, sys, screen):
        self.sys = sys
        self.screen = screen

        self.plotting_error = False

        try:
            self.this_plotter = Plotter()
            self.adr_ = self.this_plotter.get_plots_address()
        except ValueError:
            self.plotting_error = True

    def show(self):
        if not self.plotting_error:
            back_b = Button(40, 635, 150, 60, "BacK", 32)
            next_b = Button(1080, 635, 150, 60, "Next", 32)
            
            imgs = [pygame.transform.scale(pygame.image.load(i), (760, 580)) for i in self.adr_]
            imgs[-1] = pygame.transform.scale(pygame.image.load(self.adr_[-1]), (1200, 580))

            page = 0
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            running = False
                    if back_b.is_clicked(event):
                        if page > 0:
                            page -= 1
                        else:
                            running = False
                    if next_b.is_clicked(event):
                        if page < len(imgs) - 1:
                            page += 1
                    # print(page)

                self.screen.fill((0, 0, 0))
                pygame.draw.rect(self.screen, (255, 255 ,255), (0, 0, 2000, 590))
                pygame.draw.rect(self.screen, (200, 0 ,0), (0, 590, 2000, 8))

                screen_width = self.screen.get_width()
                img = imgs[page]
                x_pos = (screen_width - img.get_width()) // 2
                self.screen.blit(img, (x_pos, 0))

                back_b.create(self.screen)
                next_b.create(self.screen)
                pygame.display.flip()
        else:
            back_b = Button(40, 635, 150, 60, "BacK", 32)

            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False

                    if back_b.is_clicked(event):
                        running = False

                self.screen.fill((0, 0, 0))
                self.sys.paragraph(450, 300, 100, 100, "More data required !", (255, 255, 255), 40)
                self.sys.paragraph(120, 370, 100, 100, "You need to play at least l game and upgrade your character to view summary", (255, 255, 255), 30)

                back_b.create(self.screen)

                pygame.display.flip()