# @Time: 2021/10/19 11:34
import random
import matplotlib.pyplot as plt
_x = [i/100 for i in range(100)]
_y = [3*e+4+random.random() for e in _x]
w = random.random()
b = random.random()
#开启会话
plt.ion()
for j in range(30):
    for x,y in zip(_x,_y):
        z = w*x + b
        l = z - y
        loss = l**2
        w = -0.1*2*l*x + w
        b = -0.1*2*l + b
        print(w,b,loss)
        #清屏
        plt.cla()
        plt.plot(_x,_y,".")
        v = [w*e+b for e in _x]
        plt.plot(_x,v)
        plt.show()
        plt.pause(0.001) #暂停0.001秒
# 关闭会话
plt.ioff()
