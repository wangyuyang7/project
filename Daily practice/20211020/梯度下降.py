# @Time: 2021/10/20 17:27
import random
import numpy as np
import matplotlib.pyplot as plt
_x = [i/100 for i in range(100)]
_y = [5*e+6+random.random() for e in _x]

w = random.random()
b = random.random()
plt.ion()
for j in range(30):
    for x,y in zip(_x,_y):
        z = w*x+b
        loss = (z-y)**2
        w = -0.1*2*(z-y)*x+w
        b = -0.1*2*(z-y)+b
        print(w,b,loss)
        plt.cla()
        plt.plot(_x,_y,".")
        v = [w*e+b for e in _x]
        plt.plot(_x,v)
        plt.pause(0.001)
plt.ioff()
plt.show()

