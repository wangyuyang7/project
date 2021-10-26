# @Time: 2021/10/12 16:26
list=[5,2,7,12,6]
list1=[1,6,3,14,9]
def my_sort(my_list,flag):
    for i in range(len(my_list)-1):
        for j in range(i+1,len(my_list)):
            if flag:
                if my_list[i]>my_list[j]:
                    temp=my_list[i]
                    my_list[i]=my_list[j]
                    my_list[j]=temp
            else:
                if my_list[i]<my_list[j]:
                    temp=my_list[i]
                    my_list[i]=my_list[j]
                    my_list[j]=temp
    print(my_list)
my_sort(list,flag=True)
my_sort(list1,flag=False)