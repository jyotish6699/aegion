import time
import os

# Grid size
ROWS = 4
COLS = 5

start = (0, 0)
goal = (4, 3)

# Your path
path = [(0,0),(1,0),(2,0),(3,0),(4,0),(4,1),(4,2),(4,3)]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_grid(robot_pos):
    for y in range(ROWS):
        for x in range(COLS):
            if (x, y) == robot_pos:
                print("R", end=" ")
            elif (x, y) == start:
                print("S", end=" ")
            elif (x, y) == goal:
                print("G", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

# Animate movement
for step in path:
    clear()
    print(f"Robot at: {step}\n")
    draw_grid(step)
    time.sleep(0.6)

print("Reached Goal ✅")