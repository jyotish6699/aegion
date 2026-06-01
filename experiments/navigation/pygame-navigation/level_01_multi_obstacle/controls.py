import pygame

from obstacle import OBSTACLES

def handle_input(event, robot_row, robot_col):
    next_row = robot_row
    next_col = robot_col

    if event.key == pygame.K_UP:
        next_row -= 1

    elif event.key == pygame.K_DOWN:
        next_row += 1

    elif event.key == pygame.K_LEFT:
        next_col -= 1

    elif event.key == pygame.K_RIGHT:
        next_col += 1

    if (next_row, next_col) in OBSTACLES:
        print("Obstacle detected")
        return robot_row, robot_col
    
    return next_row, next_col