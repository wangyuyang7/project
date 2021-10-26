#不打印每个朋友的姓名，而为每人打印一条消息。
# 每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
names=["张三","李四","王五"]
for i in range(len(names)):
    message="Hello {}".format(names[i])
    print(message)
# for name in names:
#     message="Hello {}".format(name)
#     print(message)
