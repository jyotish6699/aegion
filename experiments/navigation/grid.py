GRID = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0]
]

row = len(GRID)
col = len(GRID[0])

# r = current position of row
# c = current postion in column

# Stay inside grid boundaries
def is_valid(r, c):
    return 0 <= r < row and 0 <= c < col

a = is_valid(2, 3)
b = is_valid(5, 1)
# print(a)
# print(b)

# grid[r][c] = grid[y][x]
# Avoid obstacles
def is_walkable(r, c):
    return GRID[r][c] == 0

a = is_walkable(1,1)
b = is_walkable(2,2)
# print(a)
# print(b)


# Generate next possible moves(4-direction)
def get_neighbor(r, c, debug = False):
    curr_r = r
    curr_c = c

    neighbors = []

    # directions = change in position means how much row and column change 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # [up, down, left, right] [vertical change, horizontal change]
    direction_name = ["up", "down", "left", "right"]

    i = 0

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if debug:
            print(f"Direction {direction_name[i]} -> checking ({nr}, {nc})")
            i = i + 1


        if not is_valid(nr, nc):
            if debug:
                print(f"{nr}, {nc} are INVALID")
            continue
        
        if not is_walkable(nr, nc):
            if debug:
                print(f"{nr}, {nc} are BLOCKED")
            continue

        if debug:
            print(f"{nr}, {nc} VALID AND WALKABLE")

        neighbors.append((nr, nc))
    
    return neighbors




neighbors = get_neighbor(2,2)
print(neighbors)

        

