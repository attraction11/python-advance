# pandas用于数据预处理、数据清洗
from pandas import Series, DataFrame
# import pandas as pd

obj = Series([4, 5, 6, -7])
print(obj)
print(obj.index)
print(obj.values)

# TypeError: unhashable type: 'list'
# {['a']: 1}
