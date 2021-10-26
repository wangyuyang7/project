# @Time: 2021/10/9 15:40
#在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
#修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
#再次打印一系列消息，向名单中的每位嘉宾发出邀请。
lists=["张三","李四","王五","赵六"]
for list in lists:
   message="Dear {},I want to invite you to dinner.".format(list)
   print(message)
print("张三无法赴约")
lists[0]="钱二"
for list in lists:
   new_message="Dear {},I want to invite you to dinner.".format(list)
   print(new_message)