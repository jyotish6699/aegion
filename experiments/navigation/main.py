# GRID
GRID = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

ROWS = len(GRID)
COLS = len(GRID[0])


# HELPER FUNCTION TO CHECK IF A CELL IS VALID, WALKABLE, GETS NEIGHBORS

def is_valid(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS

def is_walkable(x, y):
    return is_valid(x, y) and GRID[y][x] == 0

def get_neighbors(x, y):
    return [
        (x + 1, y),  # RIGHT
        (x - 1, y),  # LEFT
        (x, y + 1),  # DOWN
        (x, y - 1)   # UP
    ]

# print(is_valid(0, 0))  # True
# print(is_valid(-1, 0)) # False
# print(is_valid(0, -1)) # False
# print(is_valid(4, 3))  # True
# print(is_valid(5, 0))  # False
# print(is_valid(0, 4))  # False

# print(is_walkable(0, 0))  # True
# print(is_walkable(1, 1))  # False
# print(is_walkable(2, 1))  # False
# print(is_walkable(3, 1))  # False
# print(is_walkable(4, 1))  # True    


# BFS(breadth-first search) ALGORITHM

from collections import deque

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))  # (current_position, path_to_current_position)

    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path  # Return the path to the goal

        for neighbor in get_neighbors(*current):
            if neighbor not in visited:
                x, y = neighbor
                if is_walkable(x, y):
                    queue.append((neighbor, path + [neighbor]))
                    visited.add(neighbor)   

    return None  # No path found     

# SIMULATION

def move_robot(path):
    print("Moving robot along the path:")

    for step in path:
        print("Robot at:", step)


# MAIN FUNCTION

def main():
    start = (0, 0) # Starting position
    goal = (4, 3)  # Goal position

    print("Grid:")

    for row in GRID:
        print(row)

    path = bfs(start, goal)

    if path:
        print("\nPath found:", path)
        move_robot(path)
    else:
        print("\nNo path found from", start, "to", goal)


# RUN THE MAIN FUNCTION
if __name__ == "__main__":
    main()

