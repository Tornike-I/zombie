import pygame
import sys
import map
import math

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // map.COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("zombies")

clock = pygame.time.Clock()
FPS = 60

PLAYER_RADIUS = 8  # small dot

def draw_players_in_cell(row, col, num_players):
    # Determine how many dots per row in the small grid
    grid_size = math.ceil(math.sqrt(num_players))
    spacing = CELL_SIZE // (grid_size + 1)

    for i in range(num_players):
        r = i // grid_size
        c = i % grid_size
        center_x = col * CELL_SIZE + spacing * (c + 1)
        center_y = row * CELL_SIZE + spacing * (r + 1)
        pygame.draw.circle(screen, (0, 255, 0), (center_x, center_y), PLAYER_RADIUS)

# Main loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    for row in range(map.ROWS):
        for col in range(map.COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (80, 80, 80), rect, 1)

            num_players = len(map.map_grid[row][col])
            if num_players > 0:
                draw_players_in_cell(row, col, num_players)

    pygame.display.flip()

pygame.quit()
sys.exit()