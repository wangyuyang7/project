# @Time: 2021/10/26 10:26
import numpy as np
import torch

a = np.array([[[1, 2, 3], [4, 5, 6]]])
print(type(a))
print(a)
print(a.shape)
print(a.ndim)

b = torch.tensor([[[1, 2], [3, 4], [5, 6]]])
print(type(b))
print(b)
print(b.shape)
print(b.size())
