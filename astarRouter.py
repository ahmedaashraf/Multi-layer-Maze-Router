# Author : Ahmed Ashraf Taha
# email : ahmedashraf@aucegypt.edu
# created : 19.04.19
# modified : 20.04.19
# The Router


import numpy as np


class astarRouter:

    def __init__(self, grid_w, grid_h, via_cost):

        self.grid_w = grid_w
        self.grid_h = grid_h
        self.via_cost = via_cost
        self.grid = np.empty([self.grid_w, self.grid_h], dtype=int)
        for i in range(self.grid_h):
            for j in range(self.grid_w):
                self.grid[i][j] = 0

    def heuristic_function(self,source_x, source_y, source_layer, target_x, target_y, target_layer):

        dx = abs(target_x-source_x)
        dy = abs(target_y-source_y)

        return (target_layer-source_layer)+(dx+dy)

    def next_node(self,source_x, source_y, source_layer, target_x, target_y, target_layer):

        nn = 10000
        g = None
        finalnodes = []
        chosen_node = None

        if source_layer == 1:

            N = (source_x - 1, source_y , target_layer)
            W = (source_x, source_y - 1 , source_layer)
            S = (source_x + 1, source_y , target_layer)
            E = (source_x, source_y + 1 , source_layer)

            if N[0] >= 0 and self.grid[N[0]][N[1]] != target_layer+10:
                finalnodes.append(N)
            if W[1] >= 0 and self.grid[W[0]][W[1]] != source_layer+10:
                finalnodes.append(W)
            if S[0] < self.grid_h and self.grid[S[0]][S[1]] != target_layer+10:
                finalnodes.append(S)
            if E[1] < self.grid_w and self.grid[E[0]][E[1]] != source_layer+10:
                finalnodes.append(E)

        elif source_layer == 2:

            N = (source_x - 1, source_y, source_layer)
            W = (source_x, source_y - 1, target_layer)
            S = (source_x + 1, source_y, source_layer)
            E = (source_x, source_y + 1, target_layer)

            if N[0] >= 0 and self.grid[N[0]][N[1]] != source_layer+10:
                finalnodes.append(N)
            if W[1] >= 0 and self.grid[W[0]][W[1]] != target_layer+10:
                finalnodes.append(W)
            if S[0] < self.grid_h and self.grid[S[0]][S[1]] != source_layer+10:
                finalnodes.append(S)
            if E[1] < self.grid_w and self.grid[E[0]][E[1]] != target_layer+10:
                finalnodes.append(E)

        else:

            N = (source_x - 1, source_y, source_layer)
            W = (source_x, source_y - 1, target_layer)
            S = (source_x + 1, source_y, source_layer)
            E = (source_x, source_y + 1, target_layer)

            if N[0] >= 0 and self.grid[N[0]][N[1]] != target_layer+10:
                finalnodes.append(N)
            if W[1] >= 0 and self.grid[W[0]][W[1]] != source_layer+10:
                finalnodes.append(W)
            if S[0] < self.grid_h and self.grid[S[0]][S[1]] != target_layer+10:
                finalnodes.append(S)
            if E[1] < self.grid_w and self.grid[E[0]][E[1]] != source_layer+10:
                finalnodes.append(E)


        if len(finalnodes) == 0:
            print('Cannot find a next node, so cannot find a path')
        elif len(finalnodes) == 1:
            return finalnodes
        else:
            f = None
            for i in finalnodes:

                if source_layer == i[2]:

                    f = 1 + self.heuristic_function(i[0],i[1],i[2],target_x,target_y,target_layer)

                elif source_layer != i[2]:

                    f = self.via_cost+ 1 + self.heuristic_function(i[0],i[1],i[2],target_x,target_y,target_layer)

                if f < nn:
                    nn = f
                    chosen_node = i
                    g = f - self.heuristic_function(i[0],i[1],i[2],target_x,target_y,target_layer)

        return chosen_node,nn,g


    def route(self,source_x, source_y, source_layer, target_x, target_y, target_layer):

        f = []
        g = []
        h = []
        path = []
        arrived = False

        path.append([source_x, source_y, source_layer])
        g.append(0)
        h.append(self.heuristic_function(source_x, source_y, source_layer, target_x, target_y, target_layer))
        f.append(g[0]+h[0])
        if source_layer == 1:
            self.grid[source_x][source_y] = 11
        elif source_layer == 2:
            self.grid[source_x][source_y] = 12
        else: self.grid[source_x][source_y] = 13

        current_node = path[0]

        while not arrived:
            current_node_,f_val,g_val = self.next_node(current_node[0], current_node[1], current_node[2], target_x, target_y, target_layer)
            current_node = current_node_
            self.grid[current_node[0]][current_node[1]] = 10+current_node[2]
            path.append(current_node)
            f.append(f_val)
            g.append(g_val)

            if current_node == (target_x, target_y, target_layer):
                arrived = True


        return path,g,f

