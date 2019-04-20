# Author : Ahmed Ashraf Taha
# email : ahmedashraf@aucegypt.edu
# created : 20.04.19
# Test 1 , just a simple test



import matplotlib.pyplot as plt
import astarRouter
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

test = astarRouter.astarRouter(5, 5, 3)
a, b,c=test.route(0, 0, 1, 1, 2, 2)
d, e,f=test.route(0, 0, 1, 2, 1, 2)


print(" Path : " , a)
print(" g : " , b)
print(" f : " , c)
print(" ")

print(" Path : " , d)
print(" g : " , e)
print(" f : " , f)

print("\n")

plt.plot([v[0] for v in a ], [v[1] for v in a])
plt.plot([v[0] for v in d ], [v[1] for v in d])

plt.show()
print("The Grid")
test.printgrid()

