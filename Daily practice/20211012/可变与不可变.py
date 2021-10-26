# @Time: 2021/10/12 17:04
a=1
def change(a):
    a=3
change(a)
print(a)

b=[1,2,3]
def change1(b):
    b.append(4)
change1(b)
print(b)

c=[1,2]
def change2(c):
    c=[1,2,3]
change2(c)
print(c)