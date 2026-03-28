import pygame
from libs.components.ui import Button

from ..db.playerDb import PlayerStats

from ..stat import player

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

        self.in_sufficient_points = False

    def show(self):
        back_b = Button(40, 635, 150, 60, "BacK", 32)

        health_up = Button(800, 160, 170, 60, "Upgrade", 26)
        power_up = Button(800, 240, 170, 60, "Upgrade", 26)
        crit_up = Button(800, 320, 170, 60, "Upgrade", 26)
        stamina_up = Button(800, 400, 170, 60, "Upgrade", 26)
        regen_up = Button(800, 480, 170, 60, "Upgrade", 26)

        cheat_add_point = Button(450, 635, 350, 60, "lcheatl add points", 32)
        reset_progress_bt = Button(960, 635, 290, 60, "Reset Progress", 32)

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
                    self.to_upgrade('health')

                if power_up.is_clicked(event):
                    self.to_upgrade('power')
                    
                if crit_up.is_clicked(event):
                    self.to_upgrade('critical')

                if stamina_up.is_clicked(event):
                    self.to_upgrade('stamina')

                if regen_up.is_clicked(event):
                    self.to_upgrade('regen')

                if cheat_add_point.is_clicked(event):
                    self.points += 5

                if reset_progress_bt.is_clicked(event):
                    self.health = 70
                    self.power = 4
                    self.critical = 0.05
                    self.stamina = 100
                    self.stamina_regen = 1
                    self.points = 0

                    # self.sts_operator.reset_db() # this one will bomb player table

                    self.sts_operator.update(self.health, self.power, self.critical, self.stamina, self.stamina_regen, self.points)
                    print('Progress eseted')

            self.screen.fill((0, 0, 0))

            self.sys.paragraph(530, 60, 300, 100, "Upgrade", (255,255,255), 60)

            self.sys.paragraph_normal(300, 160+17, 300, 100, f"Health (cost: 10) : {self.health}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 240+17, 300, 100, f"Power (cost: 10) : {self.power}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 320+17, 300, 100, f"Critical (cost: 10) : {self.critical}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 400+17, 300, 100, f"Stamina (cost: 10) : {self.stamina}", (255,255,255), 36)
            self.sys.paragraph_normal(300, 480+17, 300, 100, f"Stamina Regen (cost: 10) : {self.stamina_regen}", (255,255,255), 36)

            self.sys.paragraph_normal(300, 560, 300, 100, f"Points : {self.points}", (255,255,0), 36)

            if self.in_sufficient_points:
                self.sys.paragraph_normal(710, 560, 300, 100, f"Insufficient Points", (200,0, 0), 36)

            health_up.create(self.screen)
            power_up.create(self.screen)
            crit_up.create(self.screen)
            stamina_up.create(self.screen)
            regen_up.create(self.screen)

            back_b.create(self.screen)
            cheat_add_point.create(self.screen)
            reset_progress_bt.create(self.screen)

            tmp_ = self.sts_operator.get_current_stat()
            player['health'] = tmp_[1]
            player['power'] = tmp_[2]
            player['critical'] = tmp_[3]
            player['stamina'] = tmp_[4]
            player['stamina_regen'] = tmp_[5]
            player['accumulative_points'] = tmp_[6]

            pygame.display.flip()

    def to_upgrade(self, name):
        if name == 'health':
            if self.points >= 10:
                self.health += 10
                self.points -= 10
                self.sts_operator.update(self.health, self.power, self.critical, self.stamina, self.stamina_regen, self.points)
                self.in_sufficient_points = False
            else:
                self.in_sufficient_points = True
                print('Insufficient Points')
        elif name == 'power':
            if self.points >= 10:
                self.power += 1
                self.points -= 10
                self.sts_operator.update(self.health, self.power, self.critical, self.stamina, self.stamina_regen, self.points)
                self.in_sufficient_points = False
            else:
                self.in_sufficient_points = True
                print('Insufficient Points')
        elif name == 'critical':
            if self.points >= 10:
                self.critical += 0.5
                self.points -= 10
                self.sts_operator.update(self.health, self.power, self.critical, self.stamina, self.stamina_regen, self.points)
                self.in_sufficient_points = False
            else:
                self.in_sufficient_points = True
                print('Insufficient Points')
        elif name == 'stamina':
            if self.points >= 10:
                self.stamina += 10
                self.points -= 10
                self.sts_operator.update(self.health, self.power, self.critical, self.stamina, self.stamina_regen, self.points)
                self.in_sufficient_points = False
            else:
                self.in_sufficient_points = True
                print('Insufficient Points')
        elif name == 'regen':
            if self.points >= 10:
                self.stamina_regen += 2
                self.points -= 10
                self.sts_operator.update(self.health, self.power, self.critical, self.stamina, self.stamina_regen, self.points)
                self.in_sufficient_points = False
            else:
                self.in_sufficient_points = True
                print('Insufficient Points')