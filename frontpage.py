import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font_large = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game - Front Page")

# Create start button
start_button_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, 50)
start_button_color = WHITE
start_button_text = font_large.render("Start Game", True, BLACK)
start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the start button is clicked
            if start_button_rect.collidepoint(event.pos):
                print("Start button clicked! (You can transition to your game here)")

    # Draw everything
    screen.fill(BLACK)

    # Draw start button
    pygame.draw.rect(screen, start_button_color, start_button_rect)
    screen.blit(start_button_text, start_button_text_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
