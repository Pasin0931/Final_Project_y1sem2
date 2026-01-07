import pygame
from libs.widgets_lib import System

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
            
        sys.draw_circle(250, 250, 250, 0, 0, 400)
        sys.draw_rect(100, 100, 100, 100, 100, 200, 400)
        
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
screen.exit()