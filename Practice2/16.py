#	定义一个列表的操作类：Listinfo
# a)	包括的方法:
# b)	1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
# c)	2 列表元素取值：get_key(num) [num:整数类型]
# d)	3 列表合并：update_list(list)      [list:列表类型]
# e)	4 删除并且返回最后一个元素：del_key()
# f)	list_info = Listinfo([44,222,111,333,454,'sss','333'])
class Listinfo():
    def __init__(self,list):
        self.list=list
    def add_key(self,keyname):
        self.list.append(keyname)
        return self.list
    def get_key(self,num):
        return self.list[num]
    def update_list(self,list1):
        self.list.extend(list1)
        return self.list
    def del_key(self):
        return self.list.pop(-1)
list_info = Listinfo([44,222,111,333,454,'sss','333'])
print(list_info.add_key("666"))
print(list_info.get_key(2))
print(list_info.update_list([777,888]))
print(list_info.del_key())
