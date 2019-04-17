import numpy as np


class SquareGrid:
    def __init__(self, grid_w, grid_h, via_cost, layer):

        self.grid_w = grid_w
        self.grid_h = grid_h
        self.via_cost = via_cost
        self.layer = layer
        self.grid = np.empty([self.grid_w, self.grid_h], dtype=int)
        for i in range(self.grid_h):
            for j in range(self.grid_w):
                self.grid[i][j] = 0

    def insert(self, row, col, val):
        if not self.occupied(row, col):
            self.grid[row][col] = val

    def remove(self, row, col):
        self.grid[row][col] = 0

    def occupied(self, row, col):
        if self.grid[row][col] != 0:
            return True

    def print(self):
        print(self.grid)



