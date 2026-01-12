import pygame
import time

from libs.system_lib import System, Background
from libs.components.ui import Button
from libs.components.menu import main_menu
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

pygame.init()
pygame.font.init()
pygame.mixer.init()

sys = System(0, 0, 0, 0, 0) # 1280, 720, 0, 0, 0

sys.initialize()

current_w, current_h = sys.get_resolution()
# print(current_w, current_h)

sys.w = current_w
sys.h = current_h

screen = sys.get_screen()

screen_status = "menu"
mu = main_menu(sys, screen, screen_status)

while mu.status != "quit":
    mu.show()
    
sys.stop()