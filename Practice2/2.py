# @Time: 2021/10/14 16:49
#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# a=1
# b=1
# c=a+b
# sum=0
# for i in range(20):
#     d=c/a
#     c=c+a
#     a=c-a
#     sum+=d
# print(sum)
a=2
b=1
sum=0
for i in range(20):
    c=a/b
    sum+=c
    d=a
    a+=b
    b=d
print(sum)