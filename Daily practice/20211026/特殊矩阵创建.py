# @Time: 2021/10/26 10:56
import torch
import numpy as np

#方阵
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# b = torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
# print(b)

#0,1矩阵
a = np.zeros((2,3))
print(a)
b = np.ones((2,3))
print(b)

c = torch.zeros(2,3)
d = torch.ones(2,3)
print(c)
print(d)

#单位矩阵
# a = np.eye(4)
# print(a)
# b = torch.eye(4)
# print(b)

# #下三角矩阵
# a = np.tri(4,4)
# print(a)
# b = torch.tril(torch.ones(4,4))
# print(b)

#对角矩阵
# a = np.diag([1,2,3,4])
# print(a)
# b = torch.diag(torch.tensor([1,2,3,4]))
# print(b)