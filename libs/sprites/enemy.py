import pygame
from ..stat import skeleton, goblin, mushroom, flying_eye

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sys, spawn_x, speed):
        super(Enemy, self).__init__()
        self.sys = sys
        self.spawn_x = spawn_x

        self.health = 30
        self.power = 30
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

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50)
        self.attack_box = pygame.Rect(0, 0, 0, 0)

    def update(self, player_pos_center):
        if not self.is_dead():
            if self.rect.centerx < player_pos_center-50:
                self.rect.x += self.speed
            elif self.rect.centerx > player_pos_center+110:
                self.rect.x -= self.speed

            self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50) # update hitbox

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