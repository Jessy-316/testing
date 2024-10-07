import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Landscape with Mario Sprite')

# Define colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)  # Sky color
GREEN = (34, 139, 34)   # Grass color
BROWN = (139, 69, 19)   # Ground color
GRAY = (128, 128, 128)  # Obstacle color

# Define physics properties
GRAVITY = 1
JUMP_STRENGTH = -20
ground_level = SCREEN_HEIGHT - 100

# Character properties
char_width = 40
char_height = 60
char_x = 100
char_y = ground_level - char_height
char_speed = 5
char_velocity_y = 0
is_jumping = False

# Load sprite sheet (using your uploaded file)
sprite_sheet = pygame.image.load('/mnt/data/image.png')

# Function to extract a single sprite from the sheet
def get_sprite(sheet, frame_x, frame_y, width, height):
    frame = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    frame.blit(sheet, (0, 0), (frame_x * width, frame_y * height, width, height))
    return frame

# Load sprites (adjust based on the dimensions of each sprite in your sheet)
sprites = []
sprite_width = 16  # Assuming each sprite is 16x16 pixels
sprite_height = 16
for i in range(0, 6):  # Assuming 6 frames for running animation
    sprites.append(get_sprite(sprite_sheet, i, 0, sprite_width, sprite_height))

# Game state variables
game_over = False
font = pygame.font.Font(None, 74)
frame_index = 0
animation_timer = 0

# Function to reset game
def reset_game():
    global char_x, char_y, char_velocity_y, is_jumping, obstacle_x, game_over
    char_x = 100
    char_y = ground_level - char_height
    char_velocity_y = 0
    is_jumping = False
    obstacle_x = SCREEN_WIDTH
    game_over = False

# Define obstacle properties
obstacle_width = 40
obstacle_height = 60
obstacle_x = SCREEN_WIDTH
obstacle_y = ground_level - obstacle_height
obstacle_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over:
        # Character movement: Jump with the Up arrow
        if keys[pygame.K_LEFT] and char_x > 0:
            char_x -= char_speed
        if keys[pygame.K_RIGHT] and char_x < SCREEN_WIDTH - char_width:
            char_x += char_speed
        if keys[pygame.K_UP] and not is_jumping:
            char_velocity_y = JUMP_STRENGTH
            is_jumping = True

        # Apply gravity
        char_velocity_y += GRAVITY
        char_y += char_velocity_y

        # Keep the character on the ground
        if char_y >= ground_level - char_height:
            char_y = ground_level - char_height
            char_velocity_y = 0
            is_jumping = False

        # Move obstacle to the left
        obstacle_x -= obstacle_speed
        if obstacle_x < -obstacle_width:
            obstacle_x = SCREEN_WIDTH  # Reset obstacle position

        # Check for collision with the obstacle
        char_rect = pygame.Rect(char_x, char_y, char_width, char_height)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        
        if char_rect.colliderect(obstacle_rect):
            game_over = True  # Collision detected, set game over

        # Animate sprite
        animation_timer += 1
        if animation_timer % 5 == 0:  # Change frame every 5 game ticks
            frame_index = (frame_index + 1) % len(sprites)

    else:
        # Display "Game Over" message
        game_over_text = font.render("Game Over! Press Enter to Restart", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3))
        pygame.display.flip()

        # Wait for the player to press Enter to restart
        if keys[pygame.K_RETURN]:
            reset_game()

    # Drawing section
    if not game_over:
        # Fill the background with sky color
        screen.fill(BLUE)

        # Draw the ground (bottom rectangle)
        ground_rect = pygame.Rect(0, ground_level, SCREEN_WIDTH, 100)
        pygame.draw.rect(screen, GREEN, ground_rect)

        # Draw the dirt (beneath the grass)
        dirt_rect = pygame.Rect(0, ground_level + 10, SCREEN_WIDTH, 10)
        pygame.draw.rect(screen, BROWN, dirt_rect)

        # Draw the obstacle (as a gray rectangle)
        pygame.draw.rect(screen, GRAY, obstacle_rect)

        # Draw the character with sprite animation
        screen.blit(pygame.transform.scale(sprites[frame_index], (char_width, char_height)), (char_x, char_y))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
