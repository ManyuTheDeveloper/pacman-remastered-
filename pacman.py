import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 30
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Pacman:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.direction = RIGHT

    def move(self):
        self.x += self.direction[0] * GRID_SIZE
        self.y += self.direction[1] * GRID_SIZE

        # Wrap around the screen
        self.x = self.x % WIDTH
        self.y = self.y % HEIGHT

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x + GRID_SIZE // 2, self.y + GRID_SIZE // 2), GRID_SIZE // 2)

class Ghost:
    def __init__(self):
        self.x = random.randint(0, WIDTH - GRID_SIZE)
        self.y = random.randint(0, HEIGHT - GRID_SIZE)
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self):
        self.x += self.direction[0] * GRID_SIZE
        self.y += self.direction[1] * GRID_SIZE

        # Wrap around the screen
        self.x = self.x % WIDTH
        self.y = self.y % HEIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, GRID_SIZE, GRID_SIZE))

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

# Create objects
pacman = Pacman()
ghost = Ghost()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pacman.direction = UP
    elif keys[pygame.K_DOWN]:
        pacman.direction = DOWN
    elif keys[pygame.K_LEFT]:
        pacman.direction = LEFT
    elif keys[pygame.K_RIGHT]:
        pacman.direction = RIGHT

    pacman.move()
    ghost.move()

    # Draw everything
    screen.fill(BLACK)
    pacman.draw(screen)
    ghost.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
