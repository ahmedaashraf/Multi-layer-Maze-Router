# Author : Ahmed Ashraf Taha
# email : ahmedashraf@aucegypt.edu
# created : 20.04.19
# Test 1



import matplotlib.pyplot as plt
import astarRouter


test = astarRouter.astarRouter(5, 5, 2)
a, b,c=test.route(0, 0, 1, 1, 2, 2)
d,e,f=test.route(0,0,2,1,2,3)

print(a)
print(b)
print(c)

print(" ")



print(d)
print(e)
print(f)

test.printgrid()



