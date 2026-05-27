import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "1200,100"

import pygame

import renderer
import robot

from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Robot Navigation")

clock = pygame.time.Clock()

running = True

while running:

    clock.tick(60)

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # MOVE UP
            if event.key == pygame.K_UP:

                if robot.robot_row > 0:
                    robot.robot_row -= 1

            # MOVE DOWN
            if event.key == pygame.K_DOWN:

                if robot.robot_row < ROWS - 1:
                    robot.robot_row += 1

            # MOVE LEFT
            if event.key == pygame.K_LEFT:

                if robot.robot_col > 0:
                    robot.robot_col -= 1

            # MOVE RIGHT
            if event.key == pygame.K_RIGHT:

                if robot.robot_col < COLS - 1:
                    robot.robot_col += 1

    # DRAW
    renderer.draw(screen)

    # GOAL CHECK
    if (
        robot.robot_row == robot.goal_row
        and
        robot.robot_col == robot.goal_col
    ):
        print("Goal Reached!")

    pygame.display.update()

pygame.quit()