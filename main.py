import pygame
import time

from libs.system_lib import System, Background
from libs.components import Button
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

play_b = Button(150, 330, 100, 60, "Play", 32)
control_b = Button(148, 430, 140, 60, "Control", 32)
summary_b = Button(140, 530, 190, 60, "Summary", 32)
quit_b = Button(150, 630, 100, 60, "Quit", 32)

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
        
        if play_b.is_clicked(event):
            print("play")
            
        if control_b.is_clicked(event):
            print("control")
            
        if summary_b.is_clicked(event):
            print("summary")
            
        if quit_b.is_clicked(event):
            print("Quit")
            running = False
            
        elif event.type == QUIT:
            running = False
            
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, dashing, jump)

    # screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(player.surf, player.rect)
    
    sys.paragraph(80, 200, 100, 100, "DarK Impact", (255, 255, 255), 80)
    
    play_b.create(screen)
    control_b.create(screen)
    summary_b.create(screen)
    quit_b.create(screen)

    pygame.display.flip()
    
sys.stop()