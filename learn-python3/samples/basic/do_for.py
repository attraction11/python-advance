#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 打印list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# 打印数字 0 - 9
for x in range(10):
    print(x)

n = 1
while n <= 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
    