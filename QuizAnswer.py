import pygame
from settings import (ANSWER_WIDTH, SCREEN_WIDTH)


class QuizAnswer:
    def __init__(self, answer, x):
        ANSWER_FONT = pygame.font.SysFont("Arial", 12)
        self.text_surface = ANSWER_FONT.render(answer, True, "black")
        self.x = x

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 255, 100), (self.x, 120, ANSWER_WIDTH, ANSWER_WIDTH))
        screen.blit(self.text_surface, (self.x + ANSWER_WIDTH / 2 - self.text_surface.get_width() / 2, 120 + ANSWER_WIDTH / 2 - self.text_surface.get_height() / 2))
    
    def is_shot(self, ammos):
        for ammo in ammos:
            if ammo.x > self.x and ammo.x < self.x + ANSWER_WIDTH and ammo.y < 120 + ANSWER_WIDTH:
                return True
        return False