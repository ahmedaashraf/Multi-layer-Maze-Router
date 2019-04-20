# Author : Ahmed Ashraf Taha
# email : ahmedashraf@aucegypt.edu
# created : 20.04.19
# Test 1



import matplotlib.pyplot as plt
import astarRouter
from mpl_toolkits import mplot3d
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')


test = astarRouter.astarRouter(5, 5, 3)
a, b,c=test.route(0, 0, 1, 1, 2, 2)
d, e,f=test.route(0, 0, 1, 2, 1, 2)


print(a)
print(b)
print(c)
print(" ")

print(d)
print(e)
print(f)


print("\n")

test.printgrid()



