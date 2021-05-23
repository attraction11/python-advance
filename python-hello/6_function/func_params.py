
# 普通函数参数的定义
# def func(a, b, c)
#     print ('a= $s' %a)
#     print ('b= $s' %b)
#     print('c= $s' % c)
# func(1, c=3)

# 取得参数的个数
# def howlong(first, *other):
#     return (1 + len(other))
# print(howlong(123, 344, 343))

# 函数作用域
var1 = 123
def func():
    global var1
    var1 = 456
    print(var1)

func()
print(var1)
