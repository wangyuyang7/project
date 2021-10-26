# @Time: 2021/10/9 16:46
#在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用 pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。
# 每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
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
print("因故只能邀请两位嘉宾共进晚餐")
i=0
for i in range(len(lists)):
    if i<5:
     messages="I'm sorry {}, I can't invite you to dinner.".format(lists[0])
     print(messages)
     lists.pop(0)
    else:
     message1="Dear {},I want to invite you to dinner.".format(lists[i-5])
     print(message1)
del lists[0]
del lists[0]
print(lists)



