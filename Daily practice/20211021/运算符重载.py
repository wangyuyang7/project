# @Time: 2021/10/21 15:27
class student():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __str__(self):
        return "姓名：{}，年龄：{}，性别：{}".format(self.name,self.age,self.sex)
p1 = student("张三",26,"男")
print(p1)
