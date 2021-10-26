# @Time: 2021/10/14 9:53
total=0
def sum(arg1,arg2):
    total=arg1+arg2
    print("局部变量",total)
    return total
sum(1,3)
print("全局变量",total)