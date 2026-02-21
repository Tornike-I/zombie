import pygame
import sys

# Initialize pygame
pygame.init()
#hehehehehehehe
# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("zombies")
# Clock (controls FPS)
clock = pygame.time.Clock()
FPS = 60

# Main game loop
running = True
while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state here

    # Draw
    screen.fill((30, 30, 30))  # Dark gray background
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (100, 100, 200, 100)
    )
    pygame.display.flip()

# Quit cleanly
pygame.quit()
sys.exit()