# @Time: 2021/10/18 17:04
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0.1,10,0.1)
y=np.log(x)
y1=np.log(x)/np.log(0.5)
plt.plot(x,y)
plt.plot(x,y1)
plt.show()

