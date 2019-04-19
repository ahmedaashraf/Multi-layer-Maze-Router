# Author : Ahmed Ashraf Taha
# email : ahmedashraf@aucegypt.edu
# modified : 19.04.19


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

    def find_path(self,source_x, source_y, source_layer, target_x, target_y, target_layer):


    def heuristic_function(self,source_x, source_y, source_layer, target_x, target_y, target_layer):

        dy = abs(target_y-source_y)
        dx = abs(target_x-source_x)
        if source_layer == 1 and target_layer == 3 or source_layer == 3 and target_layer == 1 :
            return 2*self.via_cost + (dy+dx)
        elif source_layer == 1 and target_layer == 2 or source_layer == 2 and target_layer == 1:
            return self.via_cost+(dx + dy)
        elif source_layer == 2 and target_layer == 2 or source_layer == 3 and target_layer == 2:
            return self.via_cost + (dx + dy)
        else: return 1 * (dx+dy)


    def astar(self, source_x, source_y, source_layer, target_x, target_y, target_layer):



        g = [] #Actual movement
        h = [] #Heuristic
        f = []  # f = g + h

        open_list = []  # nodes visited but not expanded
        closed_list = [] #  nodes visited and expanded
        path = set()


        open_list.append({source_x,source_y,source_layer})

        f.append(self.heuristic_function(source_x, source_y, source_layer, target_x, target_y, target_layer))

        h.append(self.heuristic_function(source_x, source_y, source_layer, target_x, target_y, target_layer))

        g.append(0)

        while len(open_list) > 0:

            current_node = None
            value = 1000
            for n in range(len(open_list)-1):     # get the lowest value for f[n] = g[n] + h[n]

                if f[n] < value:
                    value = f[n]
                    current_node = open_list[n]


            if current_node == {target_x, target_y, target_layer}:

                    return path , f





















