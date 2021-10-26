# @Time: 2021/10/12 14:37
for a in range(100,1000):
    sum = (a // 100) ** 3 + (a // 10 % 10) ** 3 + (a % 10) ** 3
    if sum == a:
     print(a)