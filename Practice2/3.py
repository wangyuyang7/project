# @Time: 2021/10/14 17:30
#求1+2!+3!+...+20!的和
a=1
b=1
sum=0
for i in range(20):
    sum+=a
    b+=1
    a=a*b
print(sum)