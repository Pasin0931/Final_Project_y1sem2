import pygame
from libs.widgets_lib import System

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_w,
    K_s,
    K_SPACE,
    QUIT
)

sys = System(900, 600, 0, 0, 0)
sys.initialize()

screen = sys.get_screen()
# sys.setBg(100, 100, 100)

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == KEYDOWN:
            if event.key == K_w:
                print("W")
                sys.draw_rect(100, 100, 100, 100, 100, 200, 400)
                
            elif event.key == K_s:
                print("S")
                sys.draw_circle(250, 250, 250, 0, 0, 400)
            
            elif event.key == K_SPACE:
                print("SPACE")
                running == False
                sys.stop()
                break
            
        pygame.display.flip()

sys.stop()