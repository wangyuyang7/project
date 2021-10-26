# @Time: 2021/10/21 16:28
import numpy as np
a = np.ndarray(12).reshape(2,2,3) #随机给数
print(a)
b = np.arange((12),dtype=np.float32).reshape(2,2,3) #范围内给数
print(b)
print(b.shape)
print(b.ndim) #维度
print(b.size)
print(b.dtype)