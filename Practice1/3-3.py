# @Time: 2021/10/9 15:25
#自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。
# 根据该列表打印一系列有关这些通勤方式的宣言
ways=["步行","自行车","地铁","公交车"]
for way in ways:
   message="My favorite way of commuting is {}.".format(way)
   print(message)