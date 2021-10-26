#  定义一个字典类：dictclass。完成下面的功能：
# a)	dict = dictclass({你需要操作的字典对象})
# b)	1 删除某个key
# c)	del_dict(key)
# d)	2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# e)	get_dict(key)
# f)	3 返回键组成的列表：返回类型;(list)
# g)	get_key()
# h)	4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# i)	update_dict({要合并的字典})
class dictclass():
    def __init__(self,dict):
        self.dict=dict
    def del_dict(self,key):
        self.dict.pop(key)
        return self.dict
    def get_dict(self,key):
        if key in self.dict:
            return self.dict(key)
        else:
            return "not found"
    def get_key(self):
        return self.dict.keys()   # 字典(Dictionary) keys()函数以列表返回一个字典所有的键。
    def update_dict(self,dict2):
        self.dict=dict(self.dict,**dict2)
        return self.dict.values()
a=dictclass({'name':'xiaoming','age':20})
print(a.del_dict('age'))
print(a.get_dict('age'))
print(a.get_key())
print(a.update_dict({"length":170}))

