#14、	定义一个学生类。有下面的类属性：
# a) 1 姓名
# b) 2 年龄
# c) 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
# d) 类方法：
# e) 1 获取学生的姓名：get_name() 返回类型:str
# f) 2 获取学生的年龄：get_age() 返回类型:int
# g) 3 返回3门科目中最高的分数。get_course() 返回类型:int
# h) 写好类以后，可以定义2个同学测试下:
# i) zm = Student('zhangming',20,[69,88,100])
# j) 返回结果：
# k) zhangming
# l) 20
# m) 100
class Student():
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def get_name(self):
        return str(self.name)
    def get_age(self):
        return int(self.age)
    def get_course(self):
        return int(max(self.course))
zm=Student('zhangming',20,[69,88,100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())