from pos_validation import is_valid, is_walkable

def get_neighbors(r, c):

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    directions_name = ["up", "down", "left", "right"]

    neighbors = []

    for dr, dc in directions:

        nr = dr + r
        nc = dc + c

        if not is_valid(nr, nc):
            continue
        
        if not is_walkable(nr, nc):
            continue

        neighbors.append((nr, nc))

    return neighbors