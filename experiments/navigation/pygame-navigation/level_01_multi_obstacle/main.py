import os
os.environ["SDL_VIDEO_WINDOW_POS"] = "1200,100"

import pygame

from config import *
from level_00_one_obstacle_avoidance.robot import *
from controls import handle_input
from level_00_one_obstacle_avoidance.renderer import draw

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Navigation System")

font = pygame.font.SysFont(None, 30)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            robot_row, robot_col = handle_input(event, robot_row, robot_col)

        robot_row = max(0, min(ROWS-1, robot_row))
        robot_col = max(0, min(COLS-1, robot_col))

        draw(
            screen,
            font,
            robot_row,
            robot_col
        )

pygame.quit()