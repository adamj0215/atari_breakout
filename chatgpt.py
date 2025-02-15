import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BRICK_WIDTH, BRICK_HEIGHT = 75, 20
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
BALL_RADIUS = 10

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Clock
clock = pygame.time.Clock()

# Paddle class
class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dx):
        self.rect.x += dx
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - PADDLE_WIDTH:
            self.rect.x = WIDTH - PADDLE_WIDTH

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.dx = random.choice([-5, 5])
        self.dy = -5

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.rect.x + BALL_RADIUS, self.rect.y + BALL_RADIUS), BALL_RADIUS)

# Brick class
class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Create bricks
def create_bricks():
    bricks = []
    for row in range(5):
        for col in range(10):
            brick = Brick(col * (BRICK_WIDTH + 5) + 35, row * (BRICK_HEIGHT + 5) + 50)
            bricks.append(brick)
    return bricks

# Main game loop
def main():
    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()
    
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-10)
        if keys[pygame.K_RIGHT]:
            paddle.move(10)

        ball.move()

        # Ball collision with walls
        if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
            ball.dx *= -1
        if ball.rect.top <= 0:
            ball.dy *= -1
        if ball.rect.bottom >= HEIGHT:
            running = False  # Game over

        # Ball collision with paddle
        if ball.rect.colliderect(paddle.rect):
            ball.dy *= -1
            ball.rect.bottom = paddle.rect.top

        # Ball collision with bricks
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.dy *= -1
                bricks.remove(brick)

        paddle.draw()
        ball.draw()
        for brick in bricks:
            brick.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
