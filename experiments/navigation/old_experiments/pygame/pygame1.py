import pygame

pygame.init()

WIDTH = 440
HEIGHT = 440

ROWS = 7
COLS = 7

CELL_SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))


# LOOP
running = True      

while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((125, 0, 0))

    for ROW in range(ROWS):
        for COL in range(COLS):
            rect = pygame.Rect(COL * CELL_SIZE, ROW * CELL_SIZE, CELL_SIZE, CELL_SIZE)    # pygame.Rect(x, y, width, height)

            if ROW == 0 or ROW == ROWS-1 or COL == 0 or COL == COLS-1:
                color = (255, 0, 0)
            else:
                color = (255, 255, 255)

            pygame.draw.rect(screen, color,  rect)   # pygame.draw.rect(surface, color, rect, width=0)

    pygame.display.update()

pygame.quit()



