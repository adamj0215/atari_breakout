import pygame
import random

class Paddle:
    def __init__(self):
        self.x = 640
        self.y = 680
        self.speed = 20

    def draw(self, screen):
        self.line = pygame.draw.line(screen, (255, 255, 255), (self.x - 60, 680), (self.x + 60, 680), 20)

    def move(self, direction):
        if direction == "left" and self.x > 60:
            self.x -= self.speed
        elif direction == "right" and self.x < 1220:
            self.x += self.speed

    def ball_collides(self, ball):
        if ball.y >= 660 and ball.y <= 667 and ball.x > self.x - 60 and ball.x < self.x + 60:
            ball.vy *= -1
        if ball.x >= self.x - 60 and ball.x <= self.x - 67 and ball.y >= 660 and ball.y <= 700:
            ball.vx *= -1
        elif ball.x <= self.x + 60 and ball.x >= self.x + 53 and ball.y >= 660 and ball.y <= 700:
            ball.vx *= -1
