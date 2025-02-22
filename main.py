import pygame
from Ball import Ball
from Paddle import Paddle
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Atari Breakout")
clock = pygame.time.Clock()
running = True

pygame.font.init()

ARIAL = pygame.font.SysFont("Arial", SCREEN_HEIGHT // 9, bold=True)

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
    
    if ball.alive:
        ball.move()
    paddle.ball_collides(ball)

    if ball.alive:
        ball.draw(screen)
    paddle.draw(screen)

    if not ball.alive:
        game_over_text = ARIAL.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over_text, (SCREEN_WIDTH / 2 - game_over_text.get_width() / 2, SCREEN_HEIGHT / 2 - game_over_text.get_height() / 2))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()