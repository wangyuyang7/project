# @Time: 2021/10/9 17:47
#尝试使用各个函数 ：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。
# 编写一个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
like=["songshan","zhongguo","chengdu","changjiang","english"]
like.append("chifan")
print(like)
like.extend(["1","2"])
print(like)
like.insert(2,"liewei")
print(like)
like[4]="huanghe"
print(like)
del like[7]
print(like)
like.pop(6)
print(like)
like.remove("2")
print(like)
like.sort()
print(like)
sorted(like)
print(like)
like.reverse()
print(like)
like.sort(reverse=True)
print(like)