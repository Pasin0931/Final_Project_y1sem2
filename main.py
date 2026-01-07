import pygame
from libs.widgets_lib import System

sys = System(800, 500)
sys.initialize()

screen = sys.set_screen(0, 0, 0)
# sys.setBg(100, 100, 100)

running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 100, 0), (0, 0), 75)
    pygame.draw.rect(screen, (100, 100, 100), (500, 300, 200, 50))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
screen.exit()