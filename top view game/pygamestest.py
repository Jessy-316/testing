import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 5
MAP_SCALE_FACTOR = 2  # Increase this factor to zoom in on the map

# Initialize game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Top-Down Adventure')

# Load images
player_image = pygame.Surface((50, 50))  # Placeholder for the player image
player_image.fill((0, 255, 0))  # Fill with green color for visibility

# Load and scale the map image
map_image = pygame.image.load('jungle_background.png')  # Replace with your actual map image filename
scaled_map_image = pygame.transform.scale(map_image, (map_image.get_width() * MAP_SCALE_FACTOR, map_image.get_height() * MAP_SCALE_FACTOR))

# Player class
class Player:
    def __init__(self):
        self.rect = player_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.world_position = [0, 0]  # Start at the top left of the map

    def move(self, dx, dy):
        # Update the world position based on movement
        self.world_position[0] += dx
        self.world_position[1] += dy

        # Keep the player within the boundaries of the scaled map
        self.world_position[0] = max(0, min(self.world_position[0], scaled_map_image.get_width() - WIDTH))
        self.world_position[1] = max(0, min(self.world_position[1], scaled_map_image.get_height() - HEIGHT))

        # Update the rectangle for drawing (keep it centered)
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def draw(self, surface):
        surface.blit(player_image, self.rect)

# Main game loop
clock = pygame.time.Clock()
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * PLAYER_SPEED

    # Move player
    player.move(dx, dy)

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background
    # Draw the scaled map, offset by the player's world position
    screen.blit(scaled_map_image, (-player.world_position[0], -player.world_position[1]))

    # Draw player
    player.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
