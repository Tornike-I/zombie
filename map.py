# map.py
import random

ROWS = 4
COLS = 4

# Each cell holds a list of players
map_grid = [[[] for _ in range(COLS)] for _ in range(ROWS)]

def random_edge_position():
    edge = random.choice(["top", "bottom", "left", "right"])
    if edge == "top":
        return 0, random.randint(0, COLS - 1)
    elif edge == "bottom":
        return ROWS - 1, random.randint(0, COLS - 1)
    elif edge == "left":
        return random.randint(0, ROWS - 1), 0
    else:
        return random.randint(0, ROWS - 1), COLS - 1

# Ask user for number of players
while True:
    try:
        NUM_PLAYERS = int(input("Enter number of players: "))
        if NUM_PLAYERS > 0:
            break
        else:
            print("Number must be positive!")
    except ValueError:
        print("Please enter a valid number.")

# Spawn all players at the same random edge cell
def spawn_players_same_cell():
    row, col = random_edge_position()
    for i in range(NUM_PLAYERS):
        map_grid[row][col].append(f"P{i+1}")

spawn_players_same_cell()