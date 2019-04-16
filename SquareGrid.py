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
        if self.layer == 1 or self.layer == 3:
            for i in range(self.grid_w):
                self.grid[self.grid_h//2][i] = self.via_cost  # needs checking, most probably wrong
        else:
            for i in range(self.grid_h):
                self.grid[i][self.grid_w//2] = self.via_cost  # needs checking, most probably wrong

    def insert(self, row, col, val):
        if self.grid[row][col] == 0:
            self.grid[row][col] = val

    def remove(self, row, col):
        self.grid[row][col] = 0

    def print(self):
        print(self.grid)


