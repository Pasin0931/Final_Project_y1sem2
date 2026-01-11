import pygame
import time

from libs.system_lib import System, Background
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
    K_d,
    K_LSHIFT,
    K_SPACE,
)

sys = System(0, 0, 0, 0, 0) # 1280, 720, 0, 0, 0

sys.initialize()

current_w, current_h = sys.get_resolution()
print(current_w, current_h)

sys.w = current_w
sys.h = current_h

screen = sys.get_screen()

player = Player(sys)

bg = Background("menu", "image").get_bg()
bg = pygame.transform.scale_by(bg, 1.1) # scale bg image up by 1.1
# screen.blit(bg, (0, 0))

running = True
while running:
    dashing = False
    jump = False
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            
            if event.key == K_LSHIFT:
                dashing = True
                
            if event.key == K_SPACE or event.key == K_w:
                print("jumping")
                jump = True
            
        elif event.type == QUIT:
            running = False
            
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, dashing, jump)

    # screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(player.surf, player.rect)
    
    sys.draw_button(80, 200, 100, 100, "DarK Impact", (255, 255, 255), 80)
    sys.draw_button(150, 330, 100, 100, "Play", (255, 255, 255), 30)
    sys.draw_button(150, 430, 100, 100, "Control", (255, 255, 255), 30)
    sys.draw_button(150, 530, 100, 100, "Summary", (255, 255, 255), 30)
    sys.draw_button(150, 630, 100, 100, "Quit", (255, 255, 255), 30)

    pygame.display.flip()
    
pygame.quit()