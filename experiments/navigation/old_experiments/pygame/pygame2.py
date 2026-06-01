import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "1200,100"

import pygame  

pygame.init()

# WINDOW
WIDTH = 440
HEIGHT = 440

ROWS = 10
COLS = 10

CELL_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Robot Navigation")

# ROBOT POSITION
robot_row = 1
robot_col = 1

# GOAL POSITION
goal_row = 5
goal_col = 5


# LOOP
running = True

while running:

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # KEYBOARD MOVEMENT
        if event.type == pygame.KEYDOWN:

            # MOVE UP
            if event.key == pygame.K_UP:
                robot_row -= 1

            # MOVE DOWN
            if event.key == pygame.K_DOWN:
                robot_row += 1

            # MOVE LEFT
            if event.key == pygame.K_LEFT:
                robot_col -= 1

            # MOVE RIGHT
            if event.key == pygame.K_RIGHT:
                robot_col += 1

    # BACKGROUND
    screen.fill((30, 30, 30))

    # DRAW GRID
    for ROW in range(ROWS):
        for COL in range(COLS):

            rect = pygame.Rect(
                COL * CELL_SIZE,
                ROW * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            # BORDER WALLS
            color = (255, 255, 255)

            # GOAL
            if ROW == goal_row and COL == goal_col:
                color = (0, 0, 255)

            # ROBOT
            if ROW == robot_row and COL == robot_col:
                color = (0, 255, 0)

            pygame.draw.rect(screen, color, rect)

            # GRID LINES
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

    # GOAL CHECK
    if robot_row == goal_row and robot_col == goal_col:
        print("Goal Reached!")

    pygame.display.update()

pygame.quit()