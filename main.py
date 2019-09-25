import pygame
import random


size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

screen2 = pygame.Surface(size)
while running:
    for event in pygame.event.get():
        screen2 = pygame.Surface(size)
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
