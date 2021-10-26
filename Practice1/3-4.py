# @Time: 2021/10/9 15:32
#嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？
# 请创建一个列表，其中包含至少 3 个你想邀请的人；
# 然后，使用这个列表打印消息，邀请这些人来与你共进晚餐。
lists=["张三","李四","王五","赵六"]
for list in lists:
   message="Dear {},I want to invite you to dinner.".format(list)
   print(message)