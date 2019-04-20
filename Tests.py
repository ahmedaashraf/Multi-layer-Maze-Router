# email : ahmedashraf@aucegypt.edu
# created : 20.04.19
# Tests , user input paths

import astarRouter
import matplotlib.pyplot as plt
import time

start = time. time()

print("Enter Path , in the following order:source row ,source col ,source layer ,target row ,target col ,target layer")

print ("To exit enter the source row as a negative number")


test = astarRouter.astarRouter(5, 5, 3)

s_r = int(input())
s_c = int(input())
s_l = int(input())
t_r = int(input())
t_c = int(input())
t_l = int(input())

while s_r >= 0:

    a, b, c = test.route(s_r, s_c, s_l, t_r, t_c, t_l)

    print(" Path : ", a)
    print(" g : ", b)
    print(" f : ", c)
    print(" ")

    print("The Grid")
    test.printgrid()

    s_r = int(input())
    s_c = int(input())
    s_l = int(input())
    t_r = int(input())
    t_c = int(input())
    t_l = int(input())


end = time. time()
print("Cpu Time",end - start)

