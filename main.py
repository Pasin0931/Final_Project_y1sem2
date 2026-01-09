import pygame

from libs.widgets_lib import System, Player

from pygame.locals import (
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
    K_d
)

sys = System(800, 600, 0, 0, 0)

sys.initialize()

screen = sys.get_screen()

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    player.update(sys, pressed_keys)

    screen.fill((0, 0, 0))
    
    screen.blit(player.surf, player.rect)

    pygame.display.flip()