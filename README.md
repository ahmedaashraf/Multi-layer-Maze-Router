# A* Multilayer Maze Router

Use astarRouter.py and Tests.py

in Tests.py :

input the coordinates one by one in the following order

1- Source row
2- Source col
3- Source layer
4- Target row
5- Target col
6- Target layer 

The output: 

For each layer you'll get the shortest path,
the values of g and f for the A* algorithm's function 
f = g + h, h is the heuristic function.

also in the end you'll get the grid which is a 2d array
in which each cell have a set of 3 elements of 0's and 1's
representing whether the cell is involved in any paths or not and if yes it is
going to be an obstacle in the future.
for example if grid[0][0] = (1,1,0) this means that this cell
is involved in a path in layer 1 and layer 2 but not 3 and this cell is an obstacle
in these layers in upcoming path findings.

also, a plot for the grid is provided
