import pygame

from settings import *
import robot


def draw(screen):

    screen.fill((30, 30, 30))

    for row in range(ROWS):
        for col in range(COLS):

            rect = pygame.Rect(
                col * CELL_SIZE,
                row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            color = (25, 255, 255)

            # GOAL
            if row == robot.goal_row and col == robot.goal_col:
                color = (0, 0, 255)

            # ROBOT
            if row == robot.robot_row and col == robot.robot_col:
                color = (0, 255, 0)

            pygame.draw.rect(screen, color, rect)

            pygame.draw.rect(screen, (0, 0, 0), rect, 1)