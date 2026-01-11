import pygame
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
        self.font_size = font_size
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = pygame.font.Font("./font/Pixelcastle-Regular.otf", font_size)

        self.base_col = (0, 0, 0, 0)
        self.text_color = (255, 255, 255)
        
        self.surface = pygame.Surface((w, h), pygame.SRCALPHA)

    # def create(self, screen): # with border filled
    #     position = pygame.mouse.get_pos()
         
    #     if self.rect.collidepoint(position):
    #         color = self.hover_color
    #     else:
    #         color = self.base_color
    #     pygame.draw.rect(screen, color, self.rect)

    #     text_surf = self.font.render(self.text, True, self.text_color)
    #     text_rect = text_surf.get_rect(center=self.rect.center)
    #     screen.blit(text_surf, text_rect)
    
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
