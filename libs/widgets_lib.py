import pygame

class System:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def set_screen(self, r, g ,b):
        self.screen = pygame.display.set_mode([self.w, self.h])
        self.screen.fill((r, g, b)) # bg color
        
        return self.screen
    
    def setBg(self, r, g, b):
        self.screen.fill((r, g, b))
    
    def initialize(self):
        pygame.init()
        
    def stop(self):
        pygame.quit()