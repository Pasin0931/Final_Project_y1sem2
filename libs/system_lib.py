import pygame

class System:
    def __init__(self, w, h, r, g, b):
        self.w = w
        self.h = h

        self.screen = pygame.display.set_mode((self.w, self.h), pygame.FULLSCREEN) # pygame.RESIZABLE
        self.screen.fill((r, g, b)) # bg color
        
        # ------------

    def get_screen(self):
        return self.screen
    
    def setBg(self, r, g, b):
        self.screen.fill((r, g, b))
        
    def draw_rect(self, r, g, b, x, y, w, h):
        pygame.draw.rect(self.screen, (r, g, b), (x, y, w, h))
        
    def draw_circle(self, r, g, b, x, y, p):
        pygame.draw.circle(self.screen, (r, g, b), (x, y), p)
        
    def draw_button(self, x, y, w, h, text, text_color, size):
        this_bt = pygame.Rect(x, y, w, h)
        font = pygame.font.Font("./font/Pixelcastle-Regular.otf", size)
        to_draw = font.render(text, True, text_color)
        to_draw.get_rect(center=this_bt.center)
        self.screen.blit(to_draw, (x, y))
        
    def add_text(self, text, text_color, size, x, y):
        # font = pygame.font.SysFont("arialblack", size)
        font = pygame.font.Font("./font/Pixelcastle-Regular.otf", size)
        to_draw = font.render(text, True, text_color)
        self.screen.blit(to_draw, (x, y))
        
    def get_info(self):
        in_ = pygame.display.Info()
        return in_
    
    def get_resolution(self):
        in_ = self.get_info()
        return in_.current_w, in_.current_h
    
    def initialize(self):
        pygame.init()
        
    def stop(self):
        pygame.quit()
        
class Background:
    def __init__(self, folder, f_name):
        self.folder = folder
        self.f_name = f_name
        
    def get_bg(self):
        b_g = pygame.image.load(f"./pictures/{self.folder}/{self.f_name}.png").convert()
        return b_g