# @Time: 2021/10/21 16:39
import numpy as np
#0数组
a = np.zeros(shape=[4,10],dtype=np.float32)
print(a)
#1数组
b = np.ones(shape=[4,10],dtype=np.float32)
print(b)
#空数组
c = np.empty(shape=[4,10],dtype=np.float32) #空并非没有，输出离他最近的数值，如果附件没有则随机生成
print(c)