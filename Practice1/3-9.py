# @Time: 2021/10/9 17:45
#使用 len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
lists=["张三","李四","王五","赵六"]
for list in lists:
   message="Dear {},I want to invite you to dinner.".format(list)
   print(message)
print(len(lists))