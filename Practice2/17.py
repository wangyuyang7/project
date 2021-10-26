#	定义一个集合的操作类：Setinfo
# a)	包括的方法:
# b)	1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
# c)	2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
# d)	3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
# e)	4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
# f)	set_info =  Setinfo(你要操作的集合)
class Setinfo():
    def __init__(self,set):
        self.set=set
    def add_setinfo(self,keyname):
        self.set.add(keyname)
        return self.set
    def get_intersection(self,unioninfo):
        return self.set & unioninfo
    def get_union(self,unioninfo):
        return self.set | unioninfo
    def del_difference(self,unioninfo):
        return self.set - unioninfo
set_info =  Setinfo({1,2,3,4})
print(set_info.add_setinfo(6))
print(set_info.get_intersection({2,4,6}))
print(set_info.get_union({2,3,5}))
print(set_info.del_difference({1,4,7}))
