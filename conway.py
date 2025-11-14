#!/usr/bin/env python3
"""
Conway's Game of Life implementation for GitHub Actions
Reads game state from game_state.txt and writes the next generation
"""

import os
from pathlib import Path

# Characters to represent cells
ALIVE = '█'
DEAD = '·'

def read_game_state(filename='game_state.txt'):
    """Read the current game state from file"""
    if not os.path.exists(filename):
        # Create initial state with a glider pattern
        return create_initial_state()

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read().strip().split('\n')

    grid = []
    for line in lines:
        row = [c == ALIVE for c in line]
        grid.append(row)

    return grid

def create_initial_state():
    """Create an initial game state with interesting patterns"""
    # 30x60 grid with a few classic patterns
    height, width = 30, 60
    grid = [[False] * width for _ in range(height)]

    # Glider (top-left)
    glider = [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
    for r, c in glider:
        if r < height and c < width:
            grid[r][c] = True

    # Blinker (middle-left)
    blinker = [(10, 5), (10, 6), (10, 7)]
    for r, c in blinker:
        if r < height and c < width:
            grid[r][c] = True

    # Toad (middle-center)
    toad = [(14, 25), (14, 26), (14, 27), (15, 24), (15, 25), (15, 26)]
    for r, c in toad:
        if r < height and c < width:
            grid[r][c] = True

    # Beacon (right side)
    beacon = [(5, 45), (5, 46), (6, 45), (6, 46),
              (7, 47), (7, 48), (8, 47), (8, 48)]
    for r, c in beacon:
        if r < height and c < width:
            grid[r][c] = True

    # Lightweight spaceship (LWSS) - bottom area
    lwss = [(25, 15), (25, 18), (26, 14), (27, 14), (28, 14), (28, 18),
            (27, 19), (26, 19), (26, 18), (26, 17), (26, 16)]
    for r, c in lwss:
        if r < height and c < width:
            grid[r][c] = True

    return grid

def count_neighbors(grid, row, col):
    """Count the number of alive neighbors for a cell"""
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    count = 0

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue

            nr, nc = row + dr, col + dc

            # Wrap around edges (toroidal topology)
            nr = nr % height
            nc = nc % width

            if grid[nr][nc]:
                count += 1

    return count

def evolve(grid):
    """Apply Conway's Game of Life rules to create the next generation"""
    if not grid or not grid[0]:
        return grid

    height = len(grid)
    width = len(grid[0])
    new_grid = [[False] * width for _ in range(height)]

    for row in range(height):
        for col in range(width):
            neighbors = count_neighbors(grid, row, col)

            if grid[row][col]:  # Cell is alive
                # Survival: 2 or 3 neighbors
                new_grid[row][col] = neighbors in [2, 3]
            else:  # Cell is dead
                # Birth: exactly 3 neighbors
                new_grid[row][col] = neighbors == 3

    return new_grid

def write_game_state(grid, filename='game_state.txt'):
    """Write the game state to file"""
    lines = []
    for row in grid:
        line = ''.join(ALIVE if cell else DEAD for cell in row)
        lines.append(line)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    """Main function to evolve the game state"""
    print("Reading current game state...")
    grid = read_game_state()

    print(f"Grid size: {len(grid)}x{len(grid[0]) if grid else 0}")

    print("Evolving to next generation...")
    new_grid = evolve(grid)

    print("Writing new game state...")
    write_game_state(new_grid)

    print("Evolution complete!")

if __name__ == '__main__':
    main()
