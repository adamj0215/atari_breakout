import pygame
import random
from settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    AMMO_RADIUS,
    PADDLE_THICKNESS,
    PADDLE_Y_FROM_BOTTOM,
    PADDLE_WIDTH
)

class Paddle:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - PADDLE_THICKNESS
        self.speed = 20

    def draw(self, screen):
        self.line = pygame.draw.line(screen, (255, 255, 255), (self.x - PADDLE_WIDTH / 2, self.y), (self.x + PADDLE_WIDTH / 2, self.y), 20)

    def move(self, direction):
        if direction == "left" and self.x > PADDLE_WIDTH / 2:
            self.x -= self.speed
        elif direction == "right" and self.x < SCREEN_WIDTH - PADDLE_WIDTH / 2:
            self.x += self.speed

    def ball_collides(self, ball):
        if ball.y >= 660 and ball.y <= 667 and ball.x > self.x - 60 and ball.x < self.x + 60:
            ball.vy *= -1
        if ball.x >= self.x - 60 and ball.x <= self.x - 67 and ball.y >= 660 and ball.y <= 700:
            ball.vx *= -1
        elif ball.x <= self.x + 60 and ball.x >= self.x + 53 and ball.y >= 660 and ball.y <= 700:
            ball.vx *= -1