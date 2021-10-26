# @Time: 2021/10/18 19:12
import random
import matplotlib.pyplot as plt
_x=[i/100 for i in range(100)]
_y=[3*e+4+random.random() for e in _x]
print(_x)
print(_y)
plt.plot(_x,_y,".")
plt.show()
