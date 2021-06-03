# 日常应用比较广泛的模块是
# 1、文字处理的re
# 2、日期类型的time、datetime
# 3、数字和数字类型的math、random
# 4、文件和目录访问的pathlib、os.path
# 5、数据压缩和归档的tarfile
# 6、通用操作系统的os、logging、argparse
# 7、多线程的threading、queue
# 8、Internet数据处理的base64、json、urllib
# 9、结构化标记处理工具html、xml
# 10、开发工具 unitest
# 11、调试工具 timeit
# 12、软件包发布venv
# 13、运行服务的__main__


# . ^ $ * + ? {m} {m,n} [] | \d \D \s ()
# ^$
# .*?
import re
p1 = re.compile('ca*t')
print(p1.match('caaaat'))

p2 = re.compile('c[bcd]t')
print(p2.match('cbt'))
