#	用代码体现继承的特点。
class Human():
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def sit(self):
        print(self.name+ " is " +self.sex+" and sitting.")
class Man(Human):
    def __init__(self,name,sex):
        super().__init__(name,sex)
action=Man("ZhangSan","male")
action.sit()

