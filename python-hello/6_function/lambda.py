# 1、普通函数的写法
def true():
    return True


# 2、精简函数写法
lambda: True

# 1、普通累加函数


def add(x, y):
    return x + y


# 2、精简lambda表达式
lambda x, y: x + y

# lambda表达式转换为普通函数
# lambda x: x <= (month, day)
# def func1(x):
#     return x <= (month, day)


# lambda item: item[1]
def func2(item):
    return item[1]

adict = {'a': 'aa', 'b': 'bb'}
for i in adict.items():
    print(func2(i))
