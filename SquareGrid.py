# Author : Ahmed Ashraf Taha
# email : ahmedashraf@aucegypt.edu
# modified : 17.04.19


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

    def heuristic_function(self,source_x, source_y, source_layer, target_x, target_y, target_layer):
            dy = abs(target_y-source_y)
            dx = abs(target_x-source_x)
            if source_layer == 1 and target_layer == 3 or source_layer == 3 and target_layer == 1 :
                return self.via_cost * (dy+dx)
            elif source_layer == 1 and target_layer == 2:
                return dx + self.via_cost*dy
            elif source_layer == 2 and target_layer == 1:
                return self.via_cost*dx + dy
            else: return 1 * (dx+dy)

    def neighbours(self,x,y):
        # does not care for layers here that is handled somewhere else


    def astar(self, source_x, source_y, source_layer, target_x, target_y, target_layer):
        # The routing

    def print(self):
        print(self.grid)


