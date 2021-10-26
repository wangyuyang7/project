# @Time: 2021/10/18 17:29
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-9.9,10,0.1)
y=1/(1+np.exp(-x))
y1=(np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
plt.plot(x,y)
plt.plot(x,y1)
plt.show()