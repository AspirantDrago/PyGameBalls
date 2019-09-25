import pygame
import random


class Ball:
    def __init__(self, pos, screen):
        self.pos = list(pos)
        self.radius = 10
        self.speed = 100
        self.r = random.randint(20, 255)
        self.g = random.randint(20, 255)
        self.b = random.randint(20, 255)
        self.color = pygame.Color(self.r, self.g, self.b)
        self.screen = screen
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

    def update(self):
        return False


size = width, height = 400, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
speed = 100
fps = 60

running = True
pos = 0, 0
screen2 = pygame.Surface(size)
balls = []
while running:
    clock.tick(fps)
    screen2.fill(pygame.Color(0, 0, 0), (0, 0, *size))
    for i in range(len(balls) - 1, -1, -1):
        if balls[i].update():
            del balls[i]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(Ball(event.pos, screen2))
    screen.blit(screen2, (0, 0))
    pygame.display.flip()
    print(balls)
pygame.quit()
