import pygame

from libs.system_lib import System
from libs.sprite_lib import Player

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
    K_d
)

sys = System(0, 0, 0, 0, 0) # 1280, 720, 0, 0, 0

sys.initialize()

current_w, current_h = sys.get_resolution()
print(current_w, current_h)

sys.w = current_w
sys.h = current_h

screen = sys.get_screen()

player = Player(sys)

bg = pygame.image.load("./pictures/stage/s1.png").convert()
# bg = pygame.image.load("./pictures/stage/s2.png").convert()
# bg = pygame.image.load("./pictures/stage/s3.png").convert()
# bg = pygame.image.load("./pictures/stage/s4.png").convert()
# bg = pygame.image.load("./pictures/stage/s5.png").convert()

bg = pygame.transform.scale_by(bg, 1.1) # scale bg image up by 1.1
# screen.blit(bg, (0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(player.surf, player.rect)

    pygame.display.flip()