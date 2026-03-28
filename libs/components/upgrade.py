import pygame
from libs.components.ui import Button

from ..db.playerDb import PlayerStats

from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    QUIT
)

class Upgrade:
    def __init__(self, sys, screen):
        self.sys = sys
        self.screen = screen

        self.sts_operator = PlayerStats()
        tmp_ = self.sts_operator.get_current_stat()

        self.health = tmp_[1]
        self.power = tmp_[2]
        self.critical = tmp_[3]
        self.stamina = tmp_[4]
        self.stamina_regen = tmp_[5]
        self.points = tmp_[6]

    def show(self):

        back_b = Button(40, 635, 150, 60, "BacK", 32)

        health_up = Button(800, 160, 170, 60, "Upgrade", 26)
        power_up = Button(800, 240, 170, 60, "Upgrade", 26)
        crit_up = Button(800, 320, 170, 60, "Upgrade", 26)
        stamina_up = Button(800, 400, 170, 60, "Upgrade", 26)
        regen_up = Button(800, 480, 170, 60, "Upgrade", 26)

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

                if health_up.is_clicked(event):
                    print("h")

                if power_up.is_clicked(event):
                    print("p")

                if crit_up.is_clicked(event):
                    print("ct")

                if stamina_up.is_clicked(event):
                    print("st")

                if regen_up.is_clicked(event):
                    print("str")

            self.screen.fill((0, 0, 0))

            self.sys.paragraph(530, 60, 300, 100, "Upgrade", (255,255,255), 60)

            self.sys.paragraph_normal(300, 160+17, 300, 100, f"Health : {self.health}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 240+17, 300, 100, f"Power : {self.power}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 320+17, 300, 100, f"Critical : {self.critical}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 400+17, 300, 100, f"Stamina : {self.stamina}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 480+17, 300, 100, f"Stamina Regen : {self.stamina_regen}", (255,255,255), 36)

            self.sys.paragraph_normal(300, 560, 300, 100, f"Points : {self.points}", (255,255,0), 36)

            health_up.create(self.screen)
            power_up.create(self.screen)
            crit_up.create(self.screen)
            stamina_up.create(self.screen)
            regen_up.create(self.screen)

            back_b.create(self.screen)

            pygame.display.flip()
