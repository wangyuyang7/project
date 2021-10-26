# @Time: 2021/10/15 19:16
#List = [-2, 1, 3, -6]，如何实现以绝对值大小从小到大将 List 中内容排序
list=[-2,1,3,-6]

# for i in range(len(list)-1):
#     for j in range(i+1,len(list)):
#         if abs(list[i])>abs(list[j]):
#            temp=list[i]
#            list[i]=list[j]
#            list[j]=temp
# print(list)

list.sort(key=abs)
print(list)


