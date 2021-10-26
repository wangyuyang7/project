# @Time: 2021/10/26 11:19
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
b = a.T
print(b)
print(b.shape)
# print(np.matmul(a,b))
c = a.dot(b)
print(c)
print(c.shape)