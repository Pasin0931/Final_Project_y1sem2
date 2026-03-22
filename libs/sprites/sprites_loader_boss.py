import pygame
import random

class Minotaur:
    def __init__(self, enemy_state):
        self.enemy_state = enemy_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/enemy/bosses/minotaur/Sprites/without_outline/ATTACK1.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/bosses/minotaur/Sprites/without_outline/ATTACK2.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/bosses/minotaur/Sprites/without_outline/DEATH.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/bosses/minotaur/Sprites/without_outline/iDLE.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/bosses/minotaur/Sprites/without_outline/WALK.png").convert_alpha())

    def get_sprite(self, x, y, w, h, index):
        if index not in [0, 1, 2, 3, 4]:
            print("index out of range")
            return
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_set[index], (0, 0), (x, y, w, h))
        return sprite
    
    def get_sprite_set(self):
        if len(self.sprite_set) != 5:
            print("sprite set not filled")
            return
        
        if self.enemy_state == 0:
            attack1 = [self.get_sprite(0, 0, 128, 115, 0),
                    self.get_sprite(128,  0, 128, 115, 0),
                    self.get_sprite(256,  0, 128, 115, 0),
                    self.get_sprite(384,  0, 128, 115, 0),
                    self.get_sprite(512,  0, 128, 115, 0),
                    self.get_sprite(640,  0, 128, 115, 0),
                    
                    self.get_sprite(0, 0, 128, 115, 3),
                    self.get_sprite(128,  0, 128, 115, 3),
                    self.get_sprite(256,  0, 128, 115, 3),
                    self.get_sprite(384,  0, 128, 115, 3),
                    self.get_sprite(512,  0, 128, 115, 3),
                    self.get_sprite(640,  0, 128, 115, 3),
                    self.get_sprite(0, 0, 128, 115, 3),
                    self.get_sprite(128,  0, 128, 115, 3),
                    self.get_sprite(256,  0, 128, 115, 3),
                    self.get_sprite(384,  0, 128, 115, 3),
                    self.get_sprite(512,  0, 128, 115, 3),
                    self.get_sprite(640,  0, 128, 115, 3)]
            return attack1
 
        elif self.enemy_state == 1:
            attack2 = [self.get_sprite(0, 0, 128, 115, 1),
                    self.get_sprite(128,  0, 128, 115, 1),
                    self.get_sprite(256,  0, 128, 115, 1),
                    self.get_sprite(384,  0, 128, 115, 1),
                    self.get_sprite(512,  0, 128, 115, 1),
                    self.get_sprite(640,  0, 128, 115, 1),
                    self.get_sprite(768,  0, 128, 115, 1),
                    
                    self.get_sprite(0, 0, 128, 115, 3),
                    self.get_sprite(128,  0, 128, 115, 3),
                    self.get_sprite(256,  0, 128, 115, 3),
                    self.get_sprite(384,  0, 128, 115, 3),
                    self.get_sprite(512,  0, 128, 115, 3),
                    self.get_sprite(640,  0, 128, 115, 3),
                    self.get_sprite(0, 0, 128, 115, 3),
                    self.get_sprite(128,  0, 128, 115, 3),
                    self.get_sprite(256,  0, 128, 115, 3),
                    self.get_sprite(384,  0, 128, 115, 3),
                    self.get_sprite(512,  0, 128, 115, 3),
                    self.get_sprite(640,  0, 128, 115, 3)]
            return attack2
        
        elif self.enemy_state == 5:
            combo_boss = []
            attack1 = [self.get_sprite(0, 0, 128, 115, 0),
                    self.get_sprite(128,  0, 128, 115, 0),
                    self.get_sprite(256,  0, 128, 115, 0),
                    self.get_sprite(384,  0, 128, 115, 0),
                    self.get_sprite(512,  0, 128, 115, 0),
                    self.get_sprite(640,  0, 128, 115, 0)]
            attack2 = [self.get_sprite(0, 0, 128, 115, 1),
                    self.get_sprite(128,  0, 128, 115, 1),
                    self.get_sprite(256,  0, 128, 115, 1),
                    self.get_sprite(384,  0, 128, 115, 1),
                    self.get_sprite(512,  0, 128, 115, 1),
                    self.get_sprite(640,  0, 128, 115, 1),
                    self.get_sprite(768,  0, 128, 115, 1),]
            idle = [self.get_sprite(0, 0, 128, 115, 3),
                    self.get_sprite(128,  0, 128, 115, 3),
                    self.get_sprite(256,  0, 128, 115, 3),
                    self.get_sprite(384,  0, 128, 115, 3),
                    self.get_sprite(512,  0, 128, 115, 3),
                    self.get_sprite(640,  0, 128, 115, 3)]
            combo_boss += ((attack1 + attack2) * 4)
            combo_boss += (idle * 5)
            return combo_boss
 
        elif self.enemy_state == 2:
            death = [self.get_sprite(0, 0, 128, 115, 2),
                    self.get_sprite(128,  0, 128, 115, 2),
                    self.get_sprite(256,  0, 128, 115, 2),
                    self.get_sprite(384,  0, 128, 115, 2),
                    self.get_sprite(512,  0, 128, 115, 2),
                    self.get_sprite(640,  0, 128, 115, 2)]
            laying = [self.get_sprite(640,  0, 128, 115, 2) for i in range(70)]
            death += laying
            return death
 
        elif self.enemy_state == 3:
            idle = [self.get_sprite(0, 0, 128, 115, 3),
                    self.get_sprite(128,  0, 128, 115, 3),
                    self.get_sprite(256,  0, 128, 115, 3),
                    self.get_sprite(384,  0, 128, 115, 3),
                    self.get_sprite(512,  0, 128, 115, 3),
                    self.get_sprite(640,  0, 128, 115, 3)]
            return idle
 
        elif self.enemy_state == 4:
            walk = [self.get_sprite(0, 0, 128, 115, 4),
                    self.get_sprite(128,  0, 128, 115, 4),
                    self.get_sprite(256,  0, 128, 115, 4),
                    self.get_sprite(384,  0, 128, 115, 4),
                    self.get_sprite(512,  0, 128, 115, 4),
                    self.get_sprite(640,  0, 128, 115, 4),
                    self.get_sprite(768,  0, 128, 115, 4),
                    self.get_sprite(896,  0, 128, 115, 4)]
            return walk
 
        else:
            raise ValueError("State out of range")

class Golem:
    def __init__(self, enemy_state):
        self.enemy_state = enemy_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/enemy/bosses/stone_golem/Sprites/without_outline/ATTACK.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/bosses/stone_golem/Sprites/without_outline/DEATH.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/bosses/stone_golem/Sprites/without_outline/IDLE.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/bosses/stone_golem/Sprites/without_outline/WALK.png").convert_alpha())

    def get_sprite(self, x, y, w, h, index):
        if index not in [0, 1, 2, 3, 4]:
            print("index out of range")
            return
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_set[index], (0, 0), (x, y, w, h))
        return sprite
    
    def get_sprite_set(self):
        if len(self.sprite_set) != 4:
            print("sprite set not filled")
            return
        
        if self.enemy_state == 0:
            attack1 = [self.get_sprite(0, 0, 220, 85, 0),
                    self.get_sprite(220,  0, 220, 85, 0),
                    self.get_sprite(220*2,  0, 220, 85, 0),
                    self.get_sprite(220*3,  0, 220, 85, 0),
                    self.get_sprite(220*4,  0, 220, 85, 0),
                    self.get_sprite(220*5,  0, 220, 85, 0),
                    self.get_sprite(220*6,  0, 220, 85, 0),
                    self.get_sprite(220*7,  0, 220, 85, 0),
                    self.get_sprite(220*8,  0, 220, 85, 0),
                    self.get_sprite(220*9,  0, 220, 85, 0),
                    self.get_sprite(220*10,  0, 220, 85, 0), # -
                    self.get_sprite(220*9,  0, 220, 85, 0),
                    self.get_sprite(220,  0, 220, 85, 0),
                    
                    self.get_sprite(0, 0, 220, 85, 2),
                    self.get_sprite(220,  0, 220, 85, 2),
                    self.get_sprite(220*2,  0, 220, 85, 2),
                    self.get_sprite(220*3,  0, 220, 85, 2),
                    self.get_sprite(220*4,  0, 220, 85, 2),
                    self.get_sprite(220*5,  0, 220, 85, 2)]
            return attack1
 
        elif self.enemy_state == 1:
            attack2 = [self.get_sprite(0, 0, 220, 85, 0),
                    self.get_sprite(220,  0, 220, 85, 0),
                    self.get_sprite(220*2,  0, 220, 85, 0),
                    self.get_sprite(220*3,  0, 220, 85, 0),
                    self.get_sprite(220*4,  0, 220, 85, 0),
                    self.get_sprite(220*5,  0, 220, 85, 0),
                    self.get_sprite(220*6,  0, 220, 85, 0),
                    self.get_sprite(220*7,  0, 220, 85, 0),
                    self.get_sprite(220*8,  0, 220, 85, 0),
                    self.get_sprite(220*9,  0, 220, 85, 0),
                    self.get_sprite(220*10,  0, 220, 85, 0),
                    self.get_sprite(220*11,  0, 220, 85, 0),
                    self.get_sprite(220*12,  0, 220, 85, 0),
                    self.get_sprite(220*13,  0, 220, 85, 0),
                    self.get_sprite(220*14,  0, 220, 85, 0),
                    self.get_sprite(220*15,  0, 220, 85, 0),
                    self.get_sprite(220*16,  0, 220, 85, 0),
                    self.get_sprite(220*17,  0, 220, 85, 0),
                    self.get_sprite(220*18,  0, 220, 85, 0),
                    self.get_sprite(220*19,  0, 220, 85, 0),

                    self.get_sprite(0, 0, 220, 85, 2),
                    self.get_sprite(220,  0, 220, 85, 2),
                    self.get_sprite(220*2,  0, 220, 85, 2),
                    self.get_sprite(220*3,  0, 220, 85, 2),
                    self.get_sprite(220*4,  0, 220, 85, 2),
                    self.get_sprite(220*5,  0, 220, 85, 2)]
            return attack2
 
        elif self.enemy_state == 2:
            death = [self.get_sprite(0, 0, 220, 85, 1),
                    self.get_sprite(220,  0, 220, 85, 1),
                    self.get_sprite(220*2,  0, 220, 85, 1),
                    self.get_sprite(220*3,  0, 220, 85, 1),
                    self.get_sprite(220*4,  0, 220, 85, 1),
                    self.get_sprite(220*5,  0, 220, 85, 1),
                    self.get_sprite(220*6,  0, 220, 85, 1),
                    self.get_sprite(220*7,  0, 220, 85, 1),
                    self.get_sprite(220*8,  0, 220, 85, 1),
                    self.get_sprite(220*9,  0, 220, 85, 1),]
            laying = [self.get_sprite(220*9,  0, 220, 85, 1) for i in range(70)]
            death += laying
            return death
 
        elif self.enemy_state == 3:
            idle = [self.get_sprite(0, 0, 220, 85, 2),
                    self.get_sprite(220,  0, 220, 85, 2),
                    self.get_sprite(220*2,  0, 220, 85, 2),
                    self.get_sprite(220*3,  0, 220, 85, 2),
                    self.get_sprite(220*4,  0, 220, 85, 2),
                    self.get_sprite(220*5,  0, 220, 85, 2)]
            return idle
 
        elif self.enemy_state == 4:
            walk = [self.get_sprite(0, 0, 220, 85, 3),
                    self.get_sprite(220,  0, 220, 85, 3),
                    self.get_sprite(220*2,  0, 220, 85, 3),
                    self.get_sprite(220*3,  0, 220, 85, 3),
                    self.get_sprite(220*4,  0, 220, 85, 3),
                    self.get_sprite(220*5,  0, 220, 85, 3),
                    self.get_sprite(220*6,  0, 220, 85, 3),
                    self.get_sprite(220*7,  0, 220, 85, 3)]
            return walk
 
        else:
            raise ValueError("State out of range")
        
class TarnishedWidow: #180.11 - 90
    def __init__(self, enemy_state):
        self.enemy_state = enemy_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/enemy/bosses/tarnished_widow/sheet.png").convert_alpha())

    def get_sprite(self, x, y, w, h, index):
        if index not in [0]:
            print("index out of range")
            return
        sprite = pygame.Surface((w, h))
        sprite = pygame.Surface((w, h), pygame.SRCALPHA)
        sprite.blit(self.sprite_set[index], (0, 0), (x, y, w, h))
        return sprite
    
    def get_sprite_set(self):
        if len(self.sprite_set) != 1:
            print("sprite set not filled")
            return
        
        if self.enemy_state == 0:
            attack1 = [self.get_sprite(0, 180, 188, 90, 0),
                    self.get_sprite(188,  180, 188, 90, 0),
                    self.get_sprite(188*2,  180, 188, 90, 0),
                    self.get_sprite(188*3,  180, 188, 90, 0),
                    self.get_sprite(188*4,  180, 188, 90, 0),
                    self.get_sprite(188*5,  180, 188, 90, 0),
                    self.get_sprite(188*6,  180, 188, 90, 0),
                    self.get_sprite(188*7,  180, 188, 90, 0),
                    self.get_sprite(188*8,  180, 188, 90, 0),
                    self.get_sprite(188*9,  180, 188, 90, 0),
                    self.get_sprite(188*10,  180, 188, 90, 0),
                    self.get_sprite(188*11,  180, 188, 90, 0),
                    self.get_sprite(188*12,  180, 188, 90, 0),
                    self.get_sprite(188*13,  180, 188, 90, 0),
                    self.get_sprite(188*14,  180, 188, 90, 0),
                    self.get_sprite(188*15,  180, 188, 90, 0),
                    self.get_sprite(188*16,  180, 188, 90, 0),
                    self.get_sprite(188*17,  180, 188, 90, 0)] # 18
            return attack1
 
        elif self.enemy_state == 1:
            attack2 = [self.get_sprite(0, 270, 188, 90, 0),
                    self.get_sprite(188,  270, 188, 90, 0),
                    self.get_sprite(188*2,  270, 188, 90, 0),
                    self.get_sprite(188*3,  270, 188, 90, 0),
                    self.get_sprite(188*4,  270, 188, 90, 0),
                    self.get_sprite(188*5,  270, 188, 90, 0),
                    self.get_sprite(188*6,  270, 188, 90, 0),
                    self.get_sprite(188*7,  270, 188, 90, 0),
                    self.get_sprite(188*8,  270, 188, 90, 0),
                    self.get_sprite(188*9,  270, 188, 90, 0),
                    self.get_sprite(188*10,  270, 188, 90, 0),
                    self.get_sprite(188*11,  270, 188, 90, 0),
                    self.get_sprite(188*12,  270, 188, 90, 0),
                    self.get_sprite(188*13,  270, 188, 90, 0),
                    self.get_sprite(188*14,  270, 188, 90, 0),
                    self.get_sprite(188*15,  270, 188, 90, 0)] # 16
            return attack2
        
        elif self.enemy_state == 2:
            jump_attack = [self.get_sprite(0, 360, 188, 90, 0),
                    self.get_sprite(188,  360, 188, 90, 0),
                    self.get_sprite(188*2,  360, 188, 90, 0),
                    self.get_sprite(188*3,  360, 188, 90, 0),
                    self.get_sprite(188*4,  360, 188, 90, 0),
                    self.get_sprite(188*5,  360, 188, 90, 0),
                    self.get_sprite(188*6,  360, 188, 90, 0),
                    self.get_sprite(188*7,  360, 188, 90, 0),
                    self.get_sprite(188*8,  360, 188, 90, 0),
                    self.get_sprite(188*9,  360, 188, 90, 0),
                    self.get_sprite(188*10,  360, 188, 90, 0),
                    self.get_sprite(188*11,  360, 188, 90, 0),
                    self.get_sprite(188*12,  360, 188, 90, 0),
                    self.get_sprite(188*13,  360, 188, 90, 0),
                    self.get_sprite(188*14,  360, 188, 90, 0), # first half
                    
                    self.get_sprite(0, 450, 188, 90, 0),
                    self.get_sprite(188,  450, 188, 90, 0),
                    self.get_sprite(188*2,  450, 188, 90, 0),
                    self.get_sprite(188*3,  450, 188, 90, 0),
                    self.get_sprite(188*4,  450, 188, 90, 0),
                    self.get_sprite(188*5,  450, 188, 90, 0),
                    self.get_sprite(188*6,  450, 188, 90, 0),
                    self.get_sprite(188*7,  450, 188, 90, 0),
                    self.get_sprite(188*8,  450, 188, 90, 0),
                    self.get_sprite(188*9,  450, 188, 90, 0),] # down
            return jump_attack
        
        elif self.enemy_state == 3:
            regen = [self.get_sprite(0, 540, 188, 90, 0),
                    self.get_sprite(188,  540, 188, 90, 0),
                    self.get_sprite(188*2,  540, 188, 90, 0),
                    self.get_sprite(188*3,  540, 188, 90, 0),
                    self.get_sprite(188*4,  540, 188, 90, 0),
                    self.get_sprite(188*5,  540, 188, 90, 0),
                    self.get_sprite(188*6,  540, 188, 90, 0),
                    self.get_sprite(188*7,  540, 188, 90, 0),
                    self.get_sprite(188*8,  540, 188, 90, 0),
                    self.get_sprite(188*9,  540, 188, 90, 0),
                    self.get_sprite(188*10,  540, 188, 90, 0),
                    self.get_sprite(188*11,  540, 188, 90, 0),
                    self.get_sprite(188*12,  540, 188, 90, 0),
                    self.get_sprite(188*13,  540, 188, 90, 0)]
            return regen
 
        elif self.enemy_state == 4:
            death = [self.get_sprite(0, 630, 188, 90, 0),
                    self.get_sprite(188,  630, 188, 90, 0),
                    self.get_sprite(188*2,  630, 188, 90, 0),
                    self.get_sprite(188*3,  630, 188, 90, 0),
                    self.get_sprite(188*4,  630, 188, 90, 0),
                    self.get_sprite(188*5,  630, 188, 90, 0),
                    self.get_sprite(188*6,  630, 188, 90, 0),
                    self.get_sprite(188*7,  630, 188, 90, 0),
                    self.get_sprite(188*8,  630, 188, 90, 0)]
            return death
 
        elif self.enemy_state == 5:
            idle = [self.get_sprite(0, 0, 188, 90, 0),
                    self.get_sprite(188,  0, 188, 90, 0),
                    self.get_sprite(188*2,  0, 188, 90, 0),
                    self.get_sprite(188*3,  0, 188, 90, 0),
                    self.get_sprite(188*4,  0, 188, 90, 0),
                    self.get_sprite(188*5,  0, 188, 90, 0),
                    self.get_sprite(188*6,  0, 188, 90, 0),
                    self.get_sprite(188*7,  0, 188, 90, 0),
                    self.get_sprite(188*8,  0, 188, 90, 0)]
            return idle
 
        elif self.enemy_state == 6:
            walk = [self.get_sprite(0, 90, 188, 90, 0),
                    self.get_sprite(188,  90, 188, 90, 0),
                    self.get_sprite(188*2,  90, 188, 90, 0),
                    self.get_sprite(188*3,  90, 188, 90, 0),
                    self.get_sprite(188*4,  90, 188, 90, 0),
                    self.get_sprite(188*5,  90, 188, 90, 0),
                    self.get_sprite(188*6,  90, 188, 90, 0),
                    self.get_sprite(188*7,  90, 188, 90, 0),
                    self.get_sprite(188*8,  90, 188, 90, 0),
                    self.get_sprite(188*9,  90, 188, 90, 0),
                    self.get_sprite(188*10,  90, 188, 90, 0)]
            return walk
 
        else:
            raise ValueError("State out of range")