# @Time: 2021/10/19 14:09
import torch
from torch import optim
import matplotlib.pyplot as plt
xs = torch.arange(0.01,1,0.01)
ys = 3*xs+4+torch.rand(99)
# print(xs,ys)
class Line(torch.nn.Module):
    #初始化模型
    def __init__(self):
        super().__init__()
        self.w = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))
    #前向计算
    def forward(self, x):
        return self.w * x + self.b
if __name__ == '__main__':
    #创建模型
    line = Line()
    #创建优化器
    # opt = optim.SGD(line.parameters(),lr=0.1) #SGD:梯度下降法。lr：步长
    opt = optim.Adam(line.parameters(),lr=0.1) #自动调整步长
    # #定义损失函数
    # loss_func = torch.nn.MSELoss()
    plt.ion()
    for i in range(30):
        for _x,_y in zip(xs,ys):
            #读取数据
            z = line.forward(_x)
            loss = (z-_y)**2
            # loss = loss_func(z,-y)

            opt.zero_grad() #清空梯度
            loss.backward()
            opt.step() #更新梯度
            print(line.w.item(),line.b.item(),loss.item())

            plt.cla()
            plt.plot(xs,ys,".")
            v = [line.w*e+line.b for e in xs]
            plt.plot(xs,v)
            plt.show()
            plt.pause(0.001)
    plt.ioff()
    plt.show()






