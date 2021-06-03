import numpy as np

arr = np.arange(10)
# arr[5:8] = 10
# print(arr)

arr_slice = arr[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr)