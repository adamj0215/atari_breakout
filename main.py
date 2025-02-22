import pygame
from Ball import Ball
from Paddle import Paddle

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Atari Breakout")
clock = pygame.time.Clock()
running = True

pygame.font.init()

ball = Ball()
paddle = Paddle()

while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move("left")
    if keys[pygame.K_RIGHT]:
        paddle.move("right")

    ball.move()

    ball.draw(screen)
    paddle.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
