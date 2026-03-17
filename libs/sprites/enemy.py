import pygame
from ..stat import skeleton, goblin, mushroom, flying_eye

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sys, spawn_x, speed):
        super(Enemy, self).__init__()
        self.sys = sys
        self.spawn_x = spawn_x

        self.health = 8
        self.power = 1
        self.critical_chance = 0.01

        self.is_alive = True
        self.is_hitted = False

        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.rect.x = self.spawn_x
        self.rect.y = sys.h // 1.3 - self.rect.height
        # self.ground_location = sys.h / 1.3

        self.speed = speed
        
        self.is_attacking = False

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

    def update(self, player_pos_center, player_is_dead):
        if not self.is_dead():
            if self.rect.centerx < player_pos_center-50:
                if not player_is_dead:
                    self.rect.x += self.speed
                self.attack_box = pygame.Rect(0, 0, 0, 0)
            elif self.rect.centerx > player_pos_center+110:
                if not player_is_dead:
                    self.rect.x -= self.speed
                self.attack_box = pygame.Rect(0, 0, 0, 0)
            else:
                self.attack(player_pos_center)

            self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50) # update hitbox

    def attack(self, player_pos):
        if player_pos > self.rect.x + 30:
            # print("attack")
            self.attack_box = pygame.Rect(self.hitbox.left, self.hitbox.y, 140, 50)
        elif player_pos < self.rect.x - 60:
            # print("attack")
            self.attack_box = pygame.Rect(self.hitbox.right-140, self.hitbox.y, 140, 50)
        else:
            self.attack_box = pygame.Rect(0, 0, 0, 0)

    def is_dead(self):
        if self.health < 0:
            self.health = 0
            self.is_alive = False
        return False

class SkeletonEnemy(Enemy):
    def __init__(self, sys):
        super().__init__(sys)

    def update(self, player_pos, is_attacking_1, is_attacking2):
        pass

# class GoblinEnemy(Enemy):
#     def __init__(self, sys):
#         super().__init__(sys)

#     def update(self, player_pos, is_attacking_1, is_attacking2):
#         pass

# class MushroomEnemy(Enemy):
#     def __init__(self, sys):
#         super().__init__(sys)

#     def update(self, player_pos, is_attacking_1, is_attacking2):
#         pass

# class FlyingEyeEnemy(Enemy):
#     def __init__(self, sys):
#         super().__init__(sys)

#     def update(self, player_pos, is_attacking_1, is_attacking2):
#         pass