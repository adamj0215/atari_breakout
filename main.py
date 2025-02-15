import pygame
from Ball import Ball

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

ball = Ball()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    ball.draw(screen)

    pygame.display.flip()

    ball.move()

    clock.tick(60)

pygame.quit()
