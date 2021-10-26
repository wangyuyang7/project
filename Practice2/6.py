# @Time: 2021/10/15 18:46
#一行代码实现对列表a中的偶数位置的元素进行加3后求和
a=[2,5,7,1,9,6]
sum1=sum(map(lambda x:x+3,a[1::2])) # map()会根据提供的函数对指定序列做映射.
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
print(sum1)