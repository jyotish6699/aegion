class GridMap:
    def init(self, grid):
        self.grid = grid
    def is_walkable(self, x, y):
        return slef.grid[x][y] == 0