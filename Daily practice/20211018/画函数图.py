# @Time: 2021/10/18 16:45
import numpy as np
import matplotlib.pyplot as plt
#定义x的值
x=np.arange(-9.9,10,0.1)
x1=np.arange(0.1,10,0.1)
x2=np.arange(-9.9,0,0.1)
y=x**2
y1=x**3
y2=x1**0.5
y3=x2**(-1)
y4=x1**(-1)
#画折线图
# plt.plot(x,y)
# plt.plot(x,y1)
# plt.plot(x1,y2)
plt.plot(x2,y3)
plt.plot(x1,y4)
#显示图像
plt.show()
