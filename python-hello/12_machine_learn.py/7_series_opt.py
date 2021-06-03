from pandas import Series, DataFrame

# 自定义值和索引key
obj = Series([4, 5, 6, -7], index=['a', 'b', 'c', 'd'])
# print(obj)

# obj['c'] = 10
# print(obj)
# print('f' in obj)

# 一维操作
sdata = {
    'beijing': 35000,
    'shanghai': 71000,
    'guangzhou': 16000,
    'shenzhen': 5000
}

obj2 = Series(sdata)
print(obj2)
obj2.index = ['bj', 'gz', 'sh', 'sz']
print(obj2)
