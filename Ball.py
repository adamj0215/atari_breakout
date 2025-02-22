import pygame
from settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    BALL_RADIUS,
    PADDLE_TOP
)

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = PADDLE_TOP - 90
        self.vx = -5
        self.vy = -5
        self.alive = True
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), BALL_RADIUS)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < BALL_RADIUS:
            self.x = BALL_RADIUS
            self.vx *= -1
        
        if self.y < BALL_RADIUS:
            self.y = BALL_RADIUS
            self.vy *= -1

        if self.x > SCREEN_WIDTH - BALL_RADIUS:
            self.x = SCREEN_WIDTH - BALL_RADIUS
            self.vx *= -1
        
        if self.y > SCREEN_HEIGHT + BALL_RADIUS:
            self.alive = False
            