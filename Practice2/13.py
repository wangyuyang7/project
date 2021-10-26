#用代码体现斐波那契数列
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))
