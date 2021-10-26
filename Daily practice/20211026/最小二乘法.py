# @Time: 2021/10/26 11:32
import numpy as np

x = np.array([[1],[2],[3]])
y = 4 * x
# print(x)
# print(y)
print(np.linalg.inv(x.T@x)) #求矩阵的逆
