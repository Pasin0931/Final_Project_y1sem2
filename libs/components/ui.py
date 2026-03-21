import pygame
from ..stat import player
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
    K_SPACE,
    K_LSHIFT
)

class Button:
    def __init__(self, x, y, w, h, text, font_size):
        pygame.font.init()
        self.font_size = font_size
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.Font("./font/Pixelcastle-Regular.otf", font_size)

        self.base_col = (0, 0, 0, 0)
        self.text_color = (255, 255, 255)
        
        self.surface = pygame.Surface((w, h), pygame.SRCALPHA)
    
    def create(self, screen):
        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            self.font = pygame.font.Font("./font/Pixelcastle-Regular.otf", self.font_size + 10)
        else:
            self.font = pygame.font.Font("./font/Pixelcastle-Regular.otf", self.font_size)
            
        self.surface.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surface, self.base_col, (0, 0, self.rect.w, self.rect.h))
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=(self.rect.w // 2, self.rect.h // 2))
        self.surface.blit(text_surf, text_rect)
        screen.blit(self.surface, self.rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                return True
        return False

class Bar:
    def __init__(self, screen, x, y, w, h):
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.w, self.h))

class HealthBar(Bar):
    def __init__(self, screen, x, y, w, h, health):
        super().__init__(screen, x, y, w, h)
        self.health = health
        self.max_health = self.w
        self.bar_color = (200, 0, 0)

    def update_health(self, curr_health):
        bar_width = (curr_health - 4)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.w+4, self.h+4)) # outlier
        pygame.draw.rect(self.screen, self.bar_color, (self.x+4, self.y+4, bar_width, self.h-4)) # health

class BossHealthBar(HealthBar):
    def __init__(self, screen, x, y, w, h, health):
        super().__init__(screen, x, y, w, h, health)
        self.max_health = health

    def update_health(self, curr_health):
        bar_width = (curr_health / self.max_health) * (self.w - 4)
        bar_width = max(0, bar_width)
        pygame.draw.rect(self.screen, (30, 30, 30), (self.x, self.y, self.w+4, self.h+4)) # outlier
        pygame.draw.rect(self.screen, (180, 0, 0), (self.x+4, self.y+4, bar_width, self.h-4)) # health
        # print(f"outline: x->{self.x}   w->{self.w+4}")
        # print(f"health:  x->{self.x+4} w->{bar_width}")

class StaminaBar(Bar):
    def __init__(self, screen, x, y, w, h, stamina):
        super().__init__(screen, x, y, w, h)
        self.stamina = stamina
        self.max_stamina = self.w
        self.bar_color = (0, 200, 0)

    def update_stamina(self, curr_stamina):
        bar_width = (curr_stamina - 4)
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.w+4, self.h+4)) # outlier
        pygame.draw.rect(self.screen, self.bar_color, (self.x+4, self.y+4, bar_width, self.h-4)) # stamina