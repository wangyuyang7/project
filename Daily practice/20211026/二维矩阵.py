# @Time: 2021/10/26 10:23
import numpy as np
import torch
a = np.array([[1,2,3],[4,5,6]])
print(type(a))
print(a)
print(a.shape) #shape里元素个数代表维度，每个元素的值代表当前维度的轴长
print(a.ndim)

b = torch.tensor([[1,2],[3,4],[5,6]])
print(type(b))
print(b)
print(b.shape)
print(b.size())