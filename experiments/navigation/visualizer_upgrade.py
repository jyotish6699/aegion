import pygame

# import bfs logic
from bfs_upgrade1 import GRID, bfs_generator

# initialize pygame
pygame.init()

# ==========================================
# WINDOW SETTINGS
# ==========================================

WIDTH = 500
HEIGHT = 500

ROWS = len(GRID)
COLS = len(GRID[0])

# size of one square
CELL_SIZE = WIDTH // COLS

# create window
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

# window title
pygame.display.set_caption(
    "LIVE BFS VISUALIZER"
)

# FPS controller
clock = pygame.time.Clock()

# ==========================================
# COLORS
# ==========================================

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

GRAY = (80, 80, 80)

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)

ORANGE = (255, 165, 0)

YELLOW = (255, 255, 0)

RED = (255, 0, 0)

# ==========================================
# START + GOAL
# ==========================================

start = (0, 0)

goal = (3, 4)

# ==========================================
# CREATE BFS GENERATOR
# ==========================================

bfs = bfs_generator(start, goal)

# ==========================================
# VISUALIZATION STORAGE
# ==========================================

# explored nodes
visited_nodes = []

# final shortest path
shortest_path = []

# error message
status_message = ""

# ==========================================
# TIMER
# ==========================================

timer = 0

# milliseconds
delay = 200

# ==========================================
# MAIN LOOP
# ==========================================

running = True

while running:

    # limit FPS
    dt = clock.tick(60)

    # accumulate elapsed time
    timer += dt

    # ==========================================
    # EVENTS
    # ==========================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    # ==========================================
    # LIVE BFS UPDATE
    # ==========================================

    if timer >= delay:

        # reset timer
        timer = 0

        try:

            # execute ONE BFS STEP
            step = next(bfs)

            # ==========================================
            # VISITING NODE
            # ==========================================

            if step["type"] == "visit":

                visited_nodes.append(
                    step["node"]
                )

            # ==========================================
            # FINAL PATH FOUND
            # ==========================================

            elif step["type"] == "path":

                shortest_path = step["path"]

                print("PATH FOUND")

            # ==========================================
            # NO PATH
            # ==========================================

            elif step["type"] == "no_path":

                status_message = "NO PATH FOUND"

                print(status_message)

            # ==========================================
            # INVALID START
            # ==========================================

            elif step["type"] == "invalid_start":

                status_message = "START IS BLOCKED"

                print(status_message)

            # ==========================================
            # INVALID GOAL
            # ==========================================

            elif step["type"] == "invalid_goal":

                status_message = "GOAL IS BLOCKED"

                print(status_message)

        except StopIteration:

            pass

    # ==========================================
    # DRAW FRAME
    # ==========================================

    screen.fill(BLACK)

    # loop through grid
    for row in range(ROWS):

        for col in range(COLS):

            # convert grid -> screen coordinate
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            rect = (
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )

            # ==========================================
            # DRAW OBSTACLE / EMPTY
            # ==========================================

            if GRID[row][col] == 1:

                pygame.draw.rect(
                    screen,
                    GRAY,
                    rect
                )

            else:

                pygame.draw.rect(
                    screen,
                    WHITE,
                    rect
                )

            # ==========================================
            # DRAW VISITED NODE
            # ==========================================

            if (row, col) in visited_nodes:

                pygame.draw.rect(
                    screen,
                    ORANGE,
                    rect
                )

            # ==========================================
            # DRAW SHORTEST PATH
            # ==========================================

            if (row, col) in shortest_path:

                pygame.draw.rect(
                    screen,
                    YELLOW,
                    rect
                )

            # ==========================================
            # DRAW START
            # ==========================================

            if (row, col) == start:

                pygame.draw.rect(
                    screen,
                    GREEN,
                    rect
                )

            # ==========================================
            # DRAW GOAL
            # ==========================================

            if (row, col) == goal:

                pygame.draw.rect(
                    screen,
                    BLUE,
                    rect
                )

            # ==========================================
            # DRAW BORDER
            # ==========================================

            pygame.draw.rect(
                screen,
                BLACK,
                rect,
                2
            )

    # update screen
    pygame.display.update()

# close pygame
pygame.quit()