from grid import *

def is_valid(r, c):
    return 0 <= r < row and 0 <= c < col 

def is_walkable(r, c):
    return GRID[r][c] == 0