# a * x + b = y

# 1、一般函数闭包的定义
# def a_line(a, b):
#     def arg_y(x):
#         return a*x+b
#     return arg_y

# 2、精简函数闭包的定义
def a_line(a, b):
    return lambda x: a*x+b

line1 = a_line(3, 5)
line2 = a_line(5, 10)
print(line1(10))
print(line1(20))
print(line2(10))
print(line2(20))
