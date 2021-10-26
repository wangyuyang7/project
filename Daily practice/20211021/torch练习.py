# @Time: 2021/10/21 11:01
import torch
from torch import optim
import matplotlib.pyplot as plt

xs = torch.arange(0,1,0.01)
ys = 3*xs+4+torch.rand(100)

class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self,x):
        return self.w*x+self.b
if __name__ == "__main__":
    line = Line()
    opt = optim.Adam(line.parameters(),lr=0.05)
    loss_func = torch.nn.MSELoss()
    plt.ion()
    for j in range(10):
        for x,y in zip(xs,ys):
            z = line.forward(x)
            loss = loss_func(z,y)
            opt.zero_grad()
            loss.backward()
            print(line.w.item(),line.b.item(),loss.item())
            opt.step()
            plt.cla()
            plt.plot(xs,ys,".")
            v = [line.w*e+line.b for e in xs]
            plt.plot(xs,v)
            plt.pause(0.0001)
    plt.ioff()
    plt.show()


