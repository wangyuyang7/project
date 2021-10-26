# @Time: 2021/10/25 19:25
import torch
import random

x1 = torch.rand(3, 4)
x2 = torch.randn(3, 4)
x3 = torch.randint(0, 4, (3, 4))

y1 = torch.rand(4)
y2 = torch.randn(4)
y3 = random.randint(0, 4)
print(x1)
print(x2)
print(x3)
print(y1)
print(y2)
print(y3)
