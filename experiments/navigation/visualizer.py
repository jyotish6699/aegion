import pygame
from bfs import GRID, path

pygame.init()

WIDTH = 500
HEIGHT = 500

ROWS = len(GRID)
COLS = len(GRID[0])

CELL_SIZE = WIDTH // COLS

# create window set_mode(width, height)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

GRAY = (80, 80, 80)

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)

# START + GOAL

start = (0, 0)
goal = (2, 2)

shortest_path, exploration_order = path(start, goal)

print(shortest_path)

# LOOP
running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(BLACK)   # fill color (RGB)
    
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            rect = (x, y, CELL_SIZE, CELL_SIZE)

            # obstacle
            if GRID[row][col] == 1:

                pygame.draw.rect(screen, GRAY, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

            # shortest path
            if(row, col) in shortest_path:
                
                pygame.draw.rect(screen, YELLOW, rect)

            # start
            if(row, col) == start:

                pygame.draw.rect(screen, GREEN, rect)

            # goal
            if(row, col) == goal:

                pygame.draw.rect(screen, BLUE, rect)

            # border
            pygame.draw.rect(screen, BLACK, rect, 2)

    pygame.display.update()

pygame.quit()