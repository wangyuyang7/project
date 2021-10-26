# @Time: 2021/10/9 16:36
#在程序末尾添加一条 print 语句，指出你找到了一个更大的餐桌。
# 使用 insert() 将一位新嘉宾添加到名单开头。
# 使用 insert() 将另一位新嘉宾添加到名单中间。
# 使用 append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。
lists=["张三","李四","王五","赵六"]
for list in lists:
   message="Dear {},I want to invite you to dinner.".format(list)
   print(message)
print("张三无法赴约")
lists[0]="钱二"
for list in lists:
   new_message="Dear {},I want to invite you to dinner.".format(list)
   print(new_message)
print("找到了一个更大的餐桌")
lists.insert(0,"唐七")
lists.insert(3,"钟八")
lists.append("刘九")
for list in lists:
   New_message="Dear {},I want to invite you to dinner.".format(list)
   print(New_message)