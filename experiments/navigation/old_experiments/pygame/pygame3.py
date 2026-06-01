import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "1200, 100"

import pygame

pygame.init()

# WINDOW
WIDTH = 500
HEIGHT = 500

robot_row = 1
robot_col = 1

ROWS = 10
COLS = 10

CELL_SIZE = WIDTH // COLS

# CREATE A SCREEN OBJECT FOR game window/display surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# CREATE A FONT OBJECT FOR RENDERING TEXT LATER
font = pygame.font.SysFont(None, 30)

running = True

while running:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_row = robot_row - 1
                next_col = robot_col

                if next_row == 5 and next_col == 5:
                    print("Obstacle detected")
                else:
                    robot_row = next_row
                    robot_col = next_col

            if event.key == pygame.K_DOWN:
                next_row = robot_row + 1
                next_col = robot_col 

                if next_row == 5 and next_col == 5:
                    print("Obstalce detected")
                else:
                    robot_col = next_col
                    robot_row = next_row

            if event.key == pygame.K_LEFT:
                next_col = robot_col - 1
                next_row = robot_row

                if next_col == 5 and next_row == 5:
                    print("Obstacle detected")
                else:
                    robot_col = next_col
                    robot_row = next_row

            if event.key == pygame.K_RIGHT:
                next_col = robot_col + 1
                next_row = robot_row

                if next_row == 5 and next_col == 5:
                    print("Obstacle detected")
                else:
                    robot_col = next_col
                    robot_row = next_row

    robot_row = max(0, min(ROWS - 1, robot_row))
    robot_col = max(0, min(COLS - 1, robot_col))


    screen.fill((0, 30, 30))

    

    for ROW in range(ROWS):
        for COL in range(COLS):
            
            rect = pygame.Rect(
                COL * CELL_SIZE,
                ROW * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE)
            
            # BORDER WALLS
            pygame.draw.rect(screen, (0, 0, 0), rect, 1)

            if ROW == robot_row and COL == robot_col:
                pygame.draw.circle(screen, (255, 34, 255), rect.center, CELL_SIZE // 2)

                # CREATE TEXT SURFACE (font.render(text, antialias, color))
                text = font.render("R", True, (255,255,255))

                # POSITION TEXT RECT AT CENTER (text.get_rect(center=rect.center))
                text_rect = text.get_rect(center=rect.center)

                # DRAW SOURCE ONTO SCREEN (screen.blit(source_surface, destination)),
                screen.blit(text, text_rect)

            if ROW == COL == 5:
                pygame.draw.rect(screen, (2, 0, 255), rect)

            
    pygame.display.update()

pygame.quit()

