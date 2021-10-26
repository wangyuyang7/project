# @Time: 2021/10/13 19:27
def outer():
    a=3 #闭包
    def inner():
        b=2 #局部
        print(a)
    inner()
outer()