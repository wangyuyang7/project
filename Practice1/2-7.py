#剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。
# 务必至少使用字符组合 "\t" 和 "\n" 各一次。
#打印这个人名，以显示其开头和末尾的空白。
# 然后，分别使用剔除函数 lstrip() 、 rstrip() 和 strip() 对人名进行处理，并将结果打印出来。
a1=" Harry Potter "
print(a1)
a2="Harry\tPotter"
print(a2)
a3="Harry\nPotter"
print(a3)
print(a1.lstrip())
print(a1.rstrip())
print(a1.strip())