import pygame

from config import *
from obstacle import OBSTACLES

def draw(screen, font, robot_row, robot_col):
    
    screen.fill(BACKGROUND_COLOR)

    for row in range(ROWS):
        for col in range(COLS):

            rect = pygame.Rect(
                col*CELL_SIZE, 
                row*CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )

            pygame.draw.rect(
                screen,
                GRID_COLOR,
                rect,
                1
            )
            
            if (row, col) in OBSTACLES:
                pygame.draw.rect(
                    screen,
                    OBSTACLE_COLOR,
                    rect
                )

            if row == robot_row and col == robot_col:
                pygame.draw.circle(
                    screen,
                    ROBOT_COLOR,
                    rect.center,
                    CELL_SIZE//2
                )

                text = font.render("R", True, TEXT_COLOR)

                text_rect = text.get_rect(
                    center=rect.center
                )

                screen.blit(text, text_rect)

    pygame.display.update()