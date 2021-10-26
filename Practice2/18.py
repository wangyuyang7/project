#将你自己的信息封装成一个类Student，包括姓名、性别、年龄、家庭地址。并在display()方法中显示这些信息。
class Student():
    def __init__(self,name,sex,age,address):
        self.name=name
        self.sex=sex
        self.age=age
        self.address=address
    def display(self):
        print("name:",self.name)
        print("sex:",self.sex)
        print("age:",self.age)
        print("address:",self.address)

Me=Student("wyy","male",27,"chengdu")
Me.display()
