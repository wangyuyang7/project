# @Time: 2021/10/26 10:29
import torch
import numpy

a = torch.tensor([[[1, 2, 2], [2, 3, 2], [4, 5, 3], [6, 3, 7]]])
print(a)
print(a.shape)
b = torch.tensor([[[3, 2, 1], [4, 3, 4], [2, 5, 3], [1, 4, 6]]])
print(b)
print(b.shape)
c = torch.tensor([[[3, 1, 5, 2], [5, 1, 7, 4], [4, 3, 5, 1]]])
print(c)
print(c.shape)
print(a + b)
print(a * b)
print(a * 3)
print(a + 3)
#张量乘法
d = torch.matmul(a, c)
# d = a@c
print(d)
print(d.shape)
