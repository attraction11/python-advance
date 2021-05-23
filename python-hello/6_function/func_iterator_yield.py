# 迭代器的使用
# list1 = [1, 2, 3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# # 发生异常: StopIteration
# print(next(it))

# for i in range(10, 20, 2):
#     print(i)

# 自定义生成器
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

# 生成器也是迭代器的一种
for i in frange(10, 20, 0.5):
    print(i)
