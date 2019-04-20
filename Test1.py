# Author : Ahmed Ashraf Taha
# email : ahmedashraf@aucegypt.edu
# created : 20.04.19
# Test 1 , just a simple test



import matplotlib.pyplot as plt
import astarRouter

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

print("The Grid")
test.printgrid()

