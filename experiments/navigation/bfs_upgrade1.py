from collections import deque

# ==========================================
# GRID MAP
# 0 = walkable
# 1 = obstacle
# ==========================================

GRID = [
    [0,0,0,0,0,1,0,0],
    [0,1,1,0,0,1,0,0],
    [0,0,0,0,1,0,0,0],
    [1,0,1,0,0,0,1,0],
    [0,0,0,0,1,0,0,0],
    [0,1,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,0,0]
]

# total rows
ROWS = len(GRID)

# total columns
COLS = len(GRID[0])

# ==========================================
# CHECK GRID BOUNDARY
# ==========================================

def is_valid(r, c):

    return 0 <= r < ROWS and 0 <= c < COLS

# ==========================================
# CHECK OBSTACLE
# ==========================================

def is_walkable(r, c):

    return GRID[r][c] == 0

# ==========================================
# GET VALID NEIGHBORS
# ==========================================

def get_neighbor(r, c):

    neighbors = []

    # up, down, left, right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        # next row
        nr = r + dr

        # next col
        nc = c + dc

        # skip invalid coordinates
        if not is_valid(nr, nc):
            continue

        # skip obstacle
        if not is_walkable(nr, nc):
            continue

        neighbors.append((nr, nc))

    return neighbors

# ==========================================
# LIVE BFS GENERATOR
# ==========================================

def bfs_generator(start, goal):

    # ==========================================
    # INVALID START / GOAL CHECK
    # ==========================================

    if not is_walkable(start[0], start[1]):

        yield {
            "type": "invalid_start"
        }

        return

    if not is_walkable(goal[0], goal[1]):

        yield {
            "type": "invalid_goal"
        }

        return

    # ==========================================
    # BFS SETUP
    # ==========================================

    queue = deque([start])

    visited = set([start])

    parent = {}

    # ==========================================
    # BFS LOOP
    # ==========================================

    while queue:

        # remove front node
        current = queue.popleft()

        # send current node to visualizer
        yield {
            "type": "visit",
            "node": current
        }

        # ==========================================
        # GOAL FOUND
        # ==========================================

        if current == goal:

            path = []

            node = goal

            # backtracking
            while node != start:

                path.append(node)

                node = parent[node]

            path.append(start)

            path.reverse()

            # send shortest path
            yield {
                "type": "path",
                "path": path
            }

            return

        # ==========================================
        # EXPLORE NEIGHBORS
        # ==========================================

        neighbors = get_neighbor(
            current[0],
            current[1]
        )

        for neighbor in neighbors:

            if neighbor not in visited:

                visited.add(neighbor)

                parent[neighbor] = current

                queue.append(neighbor)

    # ==========================================
    # NO PATH FOUND
    # ==========================================

    yield {
        "type": "no_path"
    }