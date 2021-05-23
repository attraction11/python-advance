# 异常是在出现错误时，采用正常控制流以外的动作
# 异常处理的一般流程是：检测到错误，引发异常，对异常进行捕获的操作

# 1、发生异常: NameError
# i = j

# 2、发生异常: SyntaxError
# print())

# 3、发生异常: IndexError
# a = '123'
# print(a[3])

# 4、发生异常: KeyError
# d = {'a': 1, 'b': 2}
# print(d['c'])

# 5、发生异常: ValueError
# year = int(input('input year:'))

# 6、发生异常: AttributeError
# a = 123
# a.append()

# 7、发生异常: ZeroDivisionError
# print(1 / 0)

# 捕获异常: 多种类型的
# try:
#     year = int(input('input year'))
# except (ValueError, AttributeError, KeyError):
#     print('年份要输入数字')

# 捕获异常: 打印重命名后的错误信息变量
# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print('0不能做除数%s' % e)

# 捕获异常：全部所有可能的异常情况
# try:
#     print(1 / 'a')
# except Exception as e:
#     print('%s' % e)

# 捕获异常：自定义异常
# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error')

# 捕获异常: 全流程
try:
    a = open('name1.txt')
except Exception as e:
    print(e)
finally:
    a.close()
