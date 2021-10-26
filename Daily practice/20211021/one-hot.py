# @Time: 2021/10/21 16:47
#8,5,2,6 one-hot
import numpy as np
a = np.zeros(shape=[4,10],dtype=np.float32)
for i,k in enumerate(a):
    if i == 0:
        k[8] = 1
    elif i == 1:
        k[5] = 1
    elif i == 2:
        k[2] = 1
    else:
        k[6] = 1
print(a)
b = np.argmax(a,axis=1) #取最大值的索引
print(b)




