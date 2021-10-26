# @Time: 2021/10/19 12:26
import torch
x = torch.tensor(3.0,requires_grad=True)
y = 3*x**2+4
y.backward()
print(x.grad)
