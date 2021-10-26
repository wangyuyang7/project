# @Time: 2021/10/13 18:54
def add(a,*b):
    sum=0
    for i in b:
        sum+=i
    sum1=sum+a
    return sum1

print(add(1,2,3,4,5))