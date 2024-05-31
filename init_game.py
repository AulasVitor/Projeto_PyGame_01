import pygame
import random

pygame.init()

width = 1280
heigth = 720
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()
running = True

# OBJETO 1:
obj1_dimensoes_quadrado = 50
obj1_x = (width // 2) - 100
obj1_y = heigth // 2
obj1_color = (255, 0, 0)

# OBJETO 2:
obj2_dimensoes_quadrado = 50
obj2_x = (width // 2) + 100
obj2_y = heigth // 2
obj2_color = (0, 0, 255)
obj2_hp = 100

# PISO:
piso_width = width
piso_height = 100
piso_x = 0
piso_y = heigth // 2 + 260
piso_color = (0, 255, 0)

# Movimento:
velocidade = 10