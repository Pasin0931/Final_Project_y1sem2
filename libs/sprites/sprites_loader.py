import pygame
import random
    
class Knight:
    def __init__(self, knight_state):
        self.knight_state = knight_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/player/FreeKnight_v1/Colour2/NoOutline/png120x80/_Attack.png").convert_alpha()) # 480x80
        self.add_image(pygame.image.load("./pictures/player/FreeKnight_v1/Colour2/NoOutline/png120x80/_Attack2.png").convert_alpha()) # 720x80
        self.add_image(pygame.image.load("./pictures/player/FreeKnight_v1/Colour2/NoOutline/png120x80/_AttackCombo.png").convert_alpha()) # 1200x80 --
        self.add_image(pygame.image.load("./pictures/player/FreeKnight_v1/Colour2/NoOutline/png120x80/_Roll.png").convert_alpha()) # 1440x80
        self.add_image(pygame.image.load("./pictures/player/FreeKnight_v1/Colour2/NoOutline/png120x80/_Death.png").convert_alpha()) # 1200x80 --
        self.add_image(pygame.image.load("./pictures/player/FreeKnight_v1/Colour2/NoOutline/png120x80/_Idle.png").convert_alpha()) # 1200x80 --
        self.add_image(pygame.image.load("./pictures/player/FreeKnight_v1/Colour2/NoOutline/png120x80/_Run.png").convert_alpha()) # 1200x80 --

    def get_sprite(self, x, y, w, h, index):
        if index not in [0, 1, 2, 3, 4, 5, 6]:
            print("index out of range")
            return
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_set[index], (0, 0), (x, y, w, h))
        return sprite
    
    def get_sprite_set(self):
        if len(self.sprite_set) != 7:
            print("sprite set not filled")
            return
        
        if self.knight_state == 0:
            idle = [self.get_sprite(0,    0, 120, 80, 5), # 35
                    self.get_sprite(120,  0, 120, 80, 5), # 35
                    self.get_sprite(240,  0, 120, 80, 5), # 35
                    self.get_sprite(360,  0, 120, 80, 5), # 35
                    self.get_sprite(480,  0, 120, 80, 5), # 35
                    self.get_sprite(600,  0, 120, 80, 5), # 35
                    self.get_sprite(720,  0, 120, 80, 5), # 35
                    self.get_sprite(840,  0, 120, 80, 5), # 35
                    self.get_sprite(960,  0, 120, 80, 5), # 35
                    self.get_sprite(1080, 0, 120, 80, 5)] # 35
            return idle
 
        elif self.knight_state == 1:
            run = [self.get_sprite(0,    0, 120, 80, 6),
                   self.get_sprite(120,  0, 120, 80, 6),
                   self.get_sprite(240,  0, 120, 80, 6),
                   self.get_sprite(360,  0, 120, 80, 6),
                   self.get_sprite(480,  0, 120, 80, 6),
                   self.get_sprite(600,  0, 120, 80, 6),
                   self.get_sprite(720,  0, 120, 80, 6),
                   self.get_sprite(840,  0, 120, 80, 6),
                   self.get_sprite(960,  0, 120, 80, 6),
                   self.get_sprite(1080, 0, 120, 80, 6)]
            return run
 
        elif self.knight_state == 2:
            attack1 = [self.get_sprite(0,   0, 120, 80, 0),
                       self.get_sprite(120, 0, 120, 80, 0),
                       self.get_sprite(240, 0, 120, 80, 0),
                       self.get_sprite(360, 0, 120, 80, 0)]
            return attack1
 
        elif self.knight_state == 3:
            attack2 = [self.get_sprite(0,   0, 120, 80, 1),
                       self.get_sprite(120, 0, 120, 80, 1),
                       self.get_sprite(240, 0, 120, 80, 1),
                       self.get_sprite(360, 0, 120, 80, 1),
                       self.get_sprite(480, 0, 120, 80, 1),
                       self.get_sprite(600, 0, 120, 80, 1)]
            return attack2
 
        elif self.knight_state == 4:
            combo_a = [self.get_sprite(0,    0, 120, 80, 2),
                     self.get_sprite(120,  0, 120, 80, 2),
                     self.get_sprite(240,  0, 120, 80, 2),
                     self.get_sprite(360,  0, 120, 80, 2),
                     self.get_sprite(480,  0, 120, 80, 2),
                     self.get_sprite(600,  0, 120, 80, 2),
                     self.get_sprite(720,  0, 120, 80, 2),
                     self.get_sprite(840,  0, 120, 80, 2),
                     self.get_sprite(960,  0, 120, 80, 2),
                     self.get_sprite(1080, 0, 120, 80, 2)]
            combo_b = [self.get_sprite(480,  0, 120, 80, 2),
                     self.get_sprite(600,  0, 120, 80, 2),
                     self.get_sprite(720,  0, 120, 80, 2),
                     self.get_sprite(840,  0, 120, 80, 2),
                     self.get_sprite(960,  0, 120, 80, 2),
                     self.get_sprite(1080, 0, 120, 80, 2),
                     self.get_sprite(0,    0, 120, 80, 2),
                     self.get_sprite(120,  0, 120, 80, 2),
                     self.get_sprite(240,  0, 120, 80, 2),
                     self.get_sprite(360,  0, 120, 80, 2),]
            return random.choice([combo_a, combo_b])
 
        elif self.knight_state == 5:
            death = [self.get_sprite(0,    0, 120, 80, 4),
                     self.get_sprite(120,  0, 120, 80, 4),
                     self.get_sprite(240,  0, 120, 80, 4),
                     self.get_sprite(360,  0, 120, 80, 4),
                     self.get_sprite(480,  0, 120, 80, 4),
                     self.get_sprite(600,  0, 120, 80, 4),
                     self.get_sprite(720,  0, 120, 80, 4),
                     self.get_sprite(840,  0, 120, 80, 4),
                     self.get_sprite(960,  0, 120, 80, 4),
                     self.get_sprite(1080, 0, 120, 80, 4)]
            laying = [self.get_sprite(1080, 0, 120, 80, 4) for i in range(20)]
            death+=laying
            return death
 
        elif self.knight_state == 6:
            roll = [self.get_sprite(0,    0, 120, 80, 3),
                    self.get_sprite(120,  0, 120, 80, 3),
                    self.get_sprite(240,  0, 120, 80, 3),
                    self.get_sprite(360,  0, 120, 80, 3),
                    self.get_sprite(480,  0, 120, 80, 3),
                    self.get_sprite(600,  0, 120, 80, 3),
                    self.get_sprite(720,  0, 120, 80, 3),
                    self.get_sprite(840,  0, 120, 80, 3),
                    self.get_sprite(960,  0, 120, 80, 3),
                    self.get_sprite(1080, 0, 120, 80, 3),
                    self.get_sprite(1200, 0, 120, 80, 3),
                    self.get_sprite(1320, 0, 120, 80, 3)]
            return roll
 
        else:
            raise ValueError("State out of range")
        
class FemaleKnight:
    def __init__(self, knight_state):
        self.knight_state = knight_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/player/Warrior/SpriteSheet/Warrior_Sheet-Effect.png").convert_alpha())

    def get_sprite(self, x, y, w, h, index):
        if index not in [0, 1, 2, 3, 4, 5, 6]:
            print("index out of range")
            return
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_set[index], (0, 0), (x, y, w, h))
        return sprite
    
    def get_sprite_set(self):
        if len(self.sprite_set) != 1:
            print("sprite set not filled")
            return
        
        if self.knight_state == 0:
            idle = [self.get_sprite(0,   0, 69, 44, 0),
                    self.get_sprite(69,  0, 69, 44, 0),
                    self.get_sprite(138, 0, 69, 44, 0),
                    self.get_sprite(207, 0, 69, 44, 0),
                    self.get_sprite(276, 0, 69, 44, 0),
                    self.get_sprite(345, 0, 69, 44, 0)]
            return idle
 
        elif self.knight_state == 1:
            run = [self.get_sprite(0,   44,  69, 44, 0),
                   self.get_sprite(69,  44,  69, 44, 0),
                   self.get_sprite(138, 44,  69, 44, 0),
                   self.get_sprite(207, 44,  69, 44, 0),
                   self.get_sprite(276, 44,  69, 44, 0),
                   self.get_sprite(345, 44,  69, 44, 0),
                   self.get_sprite(0,   88,  69, 44, 0),
                   self.get_sprite(69,  88,  69, 44, 0)]
            return run
 
        elif self.knight_state == 2:
            attack1 = [self.get_sprite(138, 88,  69, 44, 0),
                       self.get_sprite(207, 88,  69, 44, 0),
                       self.get_sprite(276, 88,  69, 44, 0),
                       self.get_sprite(345, 88,  69, 44, 0),
                       self.get_sprite(0,   132, 69, 44, 0),
                       self.get_sprite(69,  132, 69, 44, 0),
                       self.get_sprite(138, 132, 69, 44, 0),
                       self.get_sprite(207, 132, 69, 44, 0),
                       self.get_sprite(276, 132, 69, 44, 0),
                       self.get_sprite(345, 132, 69, 44, 0),
                       self.get_sprite(0,   176, 69, 44, 0),
                       self.get_sprite(69,  176, 69, 44, 0)]
            return attack1
 
        elif self.knight_state == 3:
            attack2 = [self.get_sprite(138, 88,  69, 44, 0),
                       self.get_sprite(345, 528, 69, 44, 0),
                       self.get_sprite(0, 572, 69, 44, 0),
                       self.get_sprite(69, 572, 69, 44, 0),
                       self.get_sprite(138, 572, 69, 44, 0),
                       self.get_sprite(207, 572, 69, 44, 0),
                       self.get_sprite(276, 572, 69, 44, 0),
                       self.get_sprite(345, 572, 69, 44, 0)]
            return attack2
 
        elif self.knight_state == 4:
            combo = [self.get_sprite(138, 88,  69, 44, 0),
                       self.get_sprite(207, 88,  69, 44, 0),
                       self.get_sprite(276, 88,  69, 44, 0),
                       self.get_sprite(345, 88,  69, 44, 0),
                       self.get_sprite(0,   132, 69, 44, 0),
                       self.get_sprite(69,  132, 69, 44, 0),
                       self.get_sprite(138, 132, 69, 44, 0),
                       self.get_sprite(207, 132, 69, 44, 0),
                       self.get_sprite(276, 132, 69, 44, 0),
                       self.get_sprite(345, 132, 69, 44, 0),
                       self.get_sprite(0,   176, 69, 44, 0),
                       self.get_sprite(69,  176, 69, 44, 0),
                       self.get_sprite(138, 88,  69, 44, 0),
                       self.get_sprite(345, 528, 69, 44, 0),
                       self.get_sprite(0, 572, 69, 44, 0),
                       self.get_sprite(69, 572, 69, 44, 0),
                       self.get_sprite(138, 572, 69, 44, 0),
                       self.get_sprite(207, 572, 69, 44, 0),
                       self.get_sprite(276, 572, 69, 44, 0),
                       self.get_sprite(345, 572, 69, 44, 0)]
            return combo
 
        elif self.knight_state == 5:
            death = [self.get_sprite(138, 176, 69, 44, 0),
                       self.get_sprite(207, 176, 69, 44, 0),
                       self.get_sprite(276, 176, 69, 44, 0),
                       self.get_sprite(345, 176, 69, 44, 0),
                       self.get_sprite(0, 220, 69, 44, 0),
                       self.get_sprite(69, 220, 69, 44, 0),
                       self.get_sprite(138, 220, 69, 44, 0),
                       self.get_sprite(207, 220, 69, 44, 0),
                       self.get_sprite(276, 220, 69, 44, 0),
                       self.get_sprite(345, 220, 69, 44, 0)]
            return death
 
        elif self.knight_state == 6:
            slide = [self.get_sprite(0,   616, 69, 44, 0),
                     self.get_sprite(69,  616, 69, 44, 0),
                     self.get_sprite(138, 616, 69, 44, 0),
                     self.get_sprite(207, 616, 69, 44, 0),
                     self.get_sprite(276, 616, 69, 44, 0),
                     self.get_sprite(138, 616, 69, 44, 0),
                     self.get_sprite(207, 616, 69, 44, 0),
                     self.get_sprite(138, 616, 69, 44, 0),
                     self.get_sprite(207, 616, 69, 44, 0),
                     self.get_sprite(276, 616, 69, 44, 0),
                     self.get_sprite(345, 616, 69, 44, 0),
                     self.get_sprite(0, 660, 69, 44, 0)]
            return slide
 
        else:
            raise ValueError("State out of range")