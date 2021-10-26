# @Time: 2021/10/12 14:01
#例：12345，输出54321
num=12345
while num>0:
    a=num%10
    print(a,end="")
    num//=10