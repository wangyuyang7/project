# @Time: 2021/10/14 10:13
def outer():
    a=1
    def inner():
        nonlocal a
        a=3
        print(a)
    inner()
    print(a)
outer()