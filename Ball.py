import pygame

class Ball:
    def __init__(self):
        self.x = 640
        self.y = 670
        self.vx = -5
        self.vy = -5
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 20)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 20:
            self.x = 20
            self.vx *= -1
        
        if self.y < 20:
            self.y = 20
            self.vy *= -1

        if self.x > 1260:
            self.x = 1260
            self.vx *= -1
        
        if self.y > 700:
            self.y = 700
            self.vy *= -1