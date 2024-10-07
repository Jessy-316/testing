import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Simple Pygame Window')

# Define colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color
    screen.fill(BLUE)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
