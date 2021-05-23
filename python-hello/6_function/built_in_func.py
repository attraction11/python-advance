# 内置函数 filter() map() reduce() zip()
from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(lambda x: x > 2, a)))

a = [1, 2, 3]
print(list(map(lambda x: x + 1, a)))

b = [4, 5, 6]
print(list(map(lambda x, y: x + y, a, b)))

print(reduce(lambda x, y: x + y, [2, 3, 4], 1))

# 类似矩阵的转换
for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)

dicta = {'a': 'aa', 'b': 'bb'}
dictb = zip(dicta.values(), dicta.keys())
print(dict(dictb))
