# @Time: 2021/10/21 15:32
def mul(a,b):
    try:
        c = a/b
        d = 'a'+1 #try中只要一个错了后面就不执行，只去执行其中一个except
        print(c)
    except ZeroDivisionError: #处理时异常
        print("除数不能为0！")
    except TypeError: #类型异常
        print("类型不统一！")
    except:
        print("出现未知错误！")

mul(1,2)
mul(3,0)
