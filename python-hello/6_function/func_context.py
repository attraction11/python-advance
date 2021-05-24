fd = open('name.txt', encoding='utf-8')

# 1、一般的异常捕获
try:
    for line in fd:
        print(line)
finally:
    fd.close

# 2、采用with上下文管理器
with open('name.txt', encoding='utf-8') as f:
    for line in f:
        print(line)
