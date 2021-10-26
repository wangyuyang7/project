# @Time: 2021/10/25 18:48
import torch
import matplotlib.pyplot as plt
from torch import nn
import random

xs = torch.unsqueeze(torch.arange(-20, 20), dim=1) / 20
ys = [e ** 3 * random.randint(1, 5) for e in xs]
ys = torch.stack(ys)


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(1, 20),
            nn.Sigmoid(),
            nn.Linear(20, 64),
            nn.Sigmoid(),
            nn.Linear(64, 128),
            nn.Sigmoid(),
            nn.Linear(128, 64),
            nn.Sigmoid(),
            nn.Linear(64, 1),
        )

    def forward(self, x):
        return self.layer(x)


if __name__ == '__main__':
    net = Net()
    opt = torch.optim.Adam(net.parameters())
    loss_fuc = nn.MSELoss()
    for e in range(300000):
        out = net.forward(xs)
        loss = loss_fuc(out, ys)
        opt.zero_grad()
        loss.backward()
        opt.step()
        plt.ion()
        if e % 5 == 0:
            print(loss.item())
            plt.cla()
            plt.plot(xs, ys, ".")
            plt.title("loss%.4f" % loss.item())
            plt.plot(xs, out.detach())
            plt.pause(0.0001)
    plt.ioff()
    plt.show()
