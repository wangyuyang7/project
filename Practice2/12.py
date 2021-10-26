#将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{'k':'1', 'k1':'2', 'k2':'3','k3':'4' }
s="k:1|k1:2|k2:3|k3:4"
s1=s.split("|",3) #split()通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔返回num+1个参数列表
a={}
for i in s1:
    key,value=i.split(":")
    a[key]=value
print(a)

