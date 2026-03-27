import pygame
import random

class Skeleton:
    def __init__(self, enemy_state):
        self.enemy_state = enemy_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Skeleton/Attack.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Skeleton/Death.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Skeleton/Idle.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Skeleton/TakeHit.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Skeleton/Walk.png").convert_alpha())

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
            idle = [self.get_sprite(0,   0, 150, 100, 2),
                    self.get_sprite(150,  0, 150, 100, 2),
                    self.get_sprite(300, 0, 150, 100, 2),
                    self.get_sprite(450, 0, 150, 100, 2)]
            return idle
 
        elif self.enemy_state == 1:
            walk = [self.get_sprite(0,   0, 150, 100, 4),
                    self.get_sprite(150,  0, 150, 100, 4),
                    self.get_sprite(300, 0, 150, 100, 4),
                    self.get_sprite(450, 0, 150, 100, 4)]
            return walk
 
        elif self.enemy_state == 2:
            attack1 = [
                       self.get_sprite(0,   0, 150, 100, 2),
                       self.get_sprite(0, 0, 150, 100, 0),
                       self.get_sprite(150, 0, 150, 100, 0),
                       self.get_sprite(300, 0, 150, 100, 0),
                       self.get_sprite(450, 0, 150, 100, 0),
                       self.get_sprite(600,   0, 150, 100, 0),
                       self.get_sprite(750,  0, 150, 100, 0),
                       self.get_sprite(900, 0, 150, 100, 0),
                       self.get_sprite(1050, 0, 150, 100, 0),

                       self.get_sprite(0,   0, 150, 100, 2),
                       self.get_sprite(150,  0, 150, 100, 2),
                       self.get_sprite(300, 0, 150, 100, 2),
                       self.get_sprite(450, 0, 150, 100, 2)]
            return attack1
 
        elif self.enemy_state == 3:
            death = [self.get_sprite(0,   0, 150, 100, 1),
                    self.get_sprite(150,  0, 150, 100, 1),
                    self.get_sprite(300, 0, 150, 100, 1),
                    self.get_sprite(450, 0, 150, 100, 1),]
            laying = [self.get_sprite(450, 0, 150, 100, 1) for i in range(70)]
            death += laying
            return death
 
        elif self.enemy_state == 4:
            take_hit = [self.get_sprite(0,   0, 150, 100, 3),
                    self.get_sprite(150,  0, 150, 100, 3),
                    self.get_sprite(300, 0, 150, 100, 3),
                    self.get_sprite(450, 0, 150, 100, 3)]
            return take_hit
 
        else:
            raise ValueError("State out of range")

class Goblin:
    def __init__(self, enemy_state):
        self.enemy_state = enemy_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Goblin/Attack.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Goblin/Death.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Goblin/Idle.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Goblin/TakeHit.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Goblin/Run.png").convert_alpha())

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
            idle = [self.get_sprite(0,   0, 150, 100, 2),
                    self.get_sprite(150,  0, 150, 100, 2),
                    self.get_sprite(300, 0, 150, 100, 2),
                    self.get_sprite(450, 0, 150, 100, 2)]
            return idle
 
        elif self.enemy_state == 1:
            walk = [self.get_sprite(0,   0, 150, 100, 4),
                    self.get_sprite(150,  0, 150, 100, 4),
                    self.get_sprite(300, 0, 150, 100, 4),
                    self.get_sprite(450, 0, 150, 100, 4),
                    self.get_sprite(600,   0, 150, 100, 4),
                    self.get_sprite(750,  0, 150, 100, 4),
                    self.get_sprite(900, 0, 150, 100, 4),
                    self.get_sprite(1050, 0, 150, 100, 4)]
            return walk
 
        elif self.enemy_state == 2:
            random_ch = random.random()
            attack1 = [self.get_sprite(0,   0, 150, 100, 2),
                       self.get_sprite(150,  0, 150, 100, 2),
                       self.get_sprite(300, 0, 150, 100, 2),
                       self.get_sprite(450, 0, 150, 100, 2),

                       self.get_sprite(0, 0, 150, 100, 0),
                       self.get_sprite(150, 0, 150, 100, 0),
                       self.get_sprite(300, 0, 150, 100, 0),
                       self.get_sprite(450, 0, 150, 100, 0),
                       self.get_sprite(600,   0, 150, 100, 0),
                       self.get_sprite(750,  0, 150, 100, 0),
                       self.get_sprite(900, 0, 150, 100, 0),
                       self.get_sprite(1050, 0, 150, 100, 0),
                       
                       self.get_sprite(0,   0, 150, 100, 2),
                       self.get_sprite(150,  0, 150, 100, 2),
                       self.get_sprite(300, 0, 150, 100, 2),
                       self.get_sprite(450, 0, 150, 100, 2),]
            return attack1
 
        elif self.enemy_state == 3:
            death = [self.get_sprite(0,   0, 150, 100, 1),
                    self.get_sprite(150,  0, 150, 100, 1),
                    self.get_sprite(300, 0, 150, 100, 1),
                    self.get_sprite(450, 0, 150, 100, 1)]
            laying = [self.get_sprite(450, 0, 150, 100, 1) for i in range(70)]
            death += laying
            return death
 
        elif self.enemy_state == 4:
            take_hit = [self.get_sprite(0,   0, 150, 100, 3),
                    self.get_sprite(150,  0, 150, 100, 3),
                    self.get_sprite(300, 0, 150, 100, 3),
                    self.get_sprite(450, 0, 150, 100, 3)]
            return take_hit
 
        else:
            raise ValueError("State out of range")
        
class Mushroom:
    def __init__(self, enemy_state):
        self.enemy_state = enemy_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Mushroom/Attack.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Mushroom/Death.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Mushroom/Idle.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Mushroom/TakeHit.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/Mushroom/Run.png").convert_alpha())

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
            idle = [self.get_sprite(0,   0, 150, 100, 2),
                    self.get_sprite(150,  0, 150, 100, 2),
                    self.get_sprite(300, 0, 150, 100, 2),
                    self.get_sprite(450, 0, 150, 100, 2)]
            return idle
 
        elif self.enemy_state == 1:
            walk = [self.get_sprite(0, 0, 150, 100, 4),
                    self.get_sprite(150, 0, 150, 100, 4),
                    self.get_sprite(300, 0, 150, 100, 4),
                    self.get_sprite(450, 0, 150, 100, 4),
                    self.get_sprite(600,   0, 150, 100, 4),
                    self.get_sprite(750,  0, 150, 100, 4),
                    self.get_sprite(900, 0, 150, 100, 4),
                    self.get_sprite(1050, 0, 150, 100, 4)]
            return walk
 
        elif self.enemy_state == 2:
            attack1 = [self.get_sprite(0, 0, 150, 100, 0),
                       self.get_sprite(150, 0, 150, 100, 0),
                       self.get_sprite(300, 0, 150, 100, 0),
                       self.get_sprite(450, 0, 150, 100, 0),
                       self.get_sprite(600,   0, 150, 100, 0),
                       self.get_sprite(750,  0, 150, 100, 0),
                       self.get_sprite(900, 0, 150, 100, 0),
                       self.get_sprite(1050, 0, 150, 100, 0)]
            
            idle_ =   [self.get_sprite(0,   0, 150, 100, 2),
                       self.get_sprite(150,  0, 150, 100, 2),
                       self.get_sprite(300, 0, 150, 100, 2),
                       self.get_sprite(450, 0, 150, 100, 2)]
            
            idle_ *= 6
            attack1 += idle_
            
            return attack1
 
        elif self.enemy_state == 3:
            death = [self.get_sprite(0,   0, 150, 100, 1),
                    self.get_sprite(150,  0, 150, 100, 1),
                    self.get_sprite(300, 0, 150, 100, 1),
                    self.get_sprite(450, 0, 150, 100, 1)]
            laying = [self.get_sprite(450, 0, 150, 100, 1) for i in range(70)]
            death += laying
            return death
 
        elif self.enemy_state == 4:
            take_hit = [self.get_sprite(0,   0, 150, 100, 3),
                    self.get_sprite(150,  0, 150, 100, 3),
                    self.get_sprite(300, 0, 150, 100, 3),
                    self.get_sprite(450, 0, 150, 100, 3)]
            return take_hit
 
        else:
            raise ValueError("State out of range")
        
class FlyingEye:
    def __init__(self, enemy_state):
        self.enemy_state = enemy_state
        self.sprite_set = []
        self.load_sprite()

    def add_image(self, file_name):
        self.sprite_set.append(file_name)

    def load_sprite(self):
        self.add_image(pygame.image.load("./pictures/enemy/monsters/FlyingEye_/Attack.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/FlyingEye_/Death.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/FlyingEye_/Flight.png").convert_alpha())
        self.add_image(pygame.image.load("./pictures/enemy/monsters/FlyingEye_/TakeHit.png").convert_alpha())

    def get_sprite(self, x, y, w, h, index):
        if index not in [0, 1, 2, 3]:
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
            flight = [self.get_sprite(0, 0, 150, 100, 2),
                       self.get_sprite(150, 0, 150, 100, 2),
                       self.get_sprite(300, 0, 150, 100, 2),
                       self.get_sprite(450, 0, 150, 100, 2),
                       self.get_sprite(600,   0, 150, 100, 2),
                       self.get_sprite(750,  0, 150, 100, 2),
                       self.get_sprite(900, 0, 150, 100, 2),
                       self.get_sprite(1050, 0, 150, 100, 2)]
            return flight
 
        elif self.enemy_state == 1:
            take_hit = [self.get_sprite(0,   0, 150, 100, 3),
                        self.get_sprite(150,  0, 150, 100, 3),
                        self.get_sprite(300, 0, 150, 100, 3),
                        self.get_sprite(450, 0, 150, 100, 3)]
            return take_hit
 
        elif self.enemy_state == 2:
            attack1 = [self.get_sprite(0, 0, 150, 100, 0),
                       self.get_sprite(150, 0, 150, 100, 0),
                       self.get_sprite(300, 0, 150, 100, 0),
                       self.get_sprite(450, 0, 150, 100, 0),
                       self.get_sprite(600,   0, 150, 100, 0),
                       self.get_sprite(750,  0, 150, 100, 0),
                       self.get_sprite(900, 0, 150, 100, 0),
                       self.get_sprite(1050, 0, 150, 100, 0),
                       
                       self.get_sprite(0, 0, 150, 100, 2),
                       self.get_sprite(150, 0, 150, 100, 2),
                       self.get_sprite(300, 0, 150, 100, 2),
                       self.get_sprite(450, 0, 150, 100, 2),
                       self.get_sprite(600,   0, 150, 100, 2),
                       self.get_sprite(750,  0, 150, 100, 2),
                       self.get_sprite(900, 0, 150, 100, 2),
                       self.get_sprite(1050, 0, 150, 100, 2)]
            return attack1
 
        elif self.enemy_state == 3:
            death = [self.get_sprite(0,   0, 150, 100, 1),
                    self.get_sprite(150,  0, 150, 100, 1),
                    self.get_sprite(300, 0, 150, 100, 1),
                    self.get_sprite(450, 0, 150, 100, 1)]
            laying = [self.get_sprite(450, 0, 150, 100, 1) for i in range(70)]
            death += laying
            return death
 
        else:
            raise ValueError("State out of range")