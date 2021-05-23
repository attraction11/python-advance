# 读取人物名称
# import os
# print(os.getcwd())
# f = open('name.txt', encoding='utf-8')
# data = f.read()
# print(data.split('|'))

# 读取兵器名称
# f2 = open('weapon.txt', encoding='utf-8')
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1

# 读取小说文本内容
# f3 = open('sanguo.txt', encoding='GB18030')
# print(f3.read().replace('\n', ''))

# 函数是对程序逻辑进行结构化的一种编程方法
# 函数的定义和传参 (使用关键词参数)
def func(filename):
    print(open(filename, encoding='utf-8').read())
    print('test func')


func('name.txt')
