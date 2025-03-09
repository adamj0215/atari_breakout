import pygame
from settings import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    AMMO_RADIUS,
    PADDLE_TOP
)

class Ammo:
    def __init__(self, x):
        self.x = x
        self.y = PADDLE_TOP
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), AMMO_RADIUS)

    def move(self):
        self.y -= 8
