# @Time: 2021/10/22 18:33
import torch
from torch import nn
import matplotlib.pyplot as plt
import numpy as np
xs = torch.unsqueeze(torch.arange(0, 1, 0.01), dim=1)
ys = 3*xs+4+torch.rand(100)

class Line(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_layer = nn.Sequential(
            nn.Linear(1,20),
            nn.Linear(20,64),
            nn.Linear(64,128),
            nn.Linear(128,64),
            nn.Linear(64,1),
        )
    def forward(self,x):
        return self.fc_layer(x)
if __name__ == "__main__":
    net = Line()
    loss_func = nn.MSELoss()
    opt = torch.optim.Adam(net.parameters())
    plt.ion()
    for epoch in range(3000):
        z = net.forward(xs)
        loss = loss_func(z,ys)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if epoch % 5 == 0:
            print(loss.item())
            plt.cla()
            plt.plot(xs,ys,".")
            plt.title("loss%.4f"%loss.item())
            plt.plot(xs,z.detach())
            plt.pause(0.0001)
    plt.ioff()
    plt.show()

