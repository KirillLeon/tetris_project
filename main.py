# Импорт библиотек
import pygame
from copy import deepcopy
from random import choice, randrange

# Задаем неизменяемые значения
W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
RES = 750, 940
FPS = 60

# инициализация Pygame:
pygame.init()
# sc — холст, на котором нужно рисовать:
sc = pygame.display.set_mode(RES)
game_sc = pygame.Surface(GAME_RES)
clock = pygame.time.Clock()