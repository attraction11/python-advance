import re

# 1、一般匹配
# p1 = re.compile('...')
# print(p1.match('bat'))

# p2 = re.compile('.{3}')
# print(p2.match('bat'))

# 2、防止转义
# print(r'\nx\n')

# 3、分组
# p3 = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p3.match('aa2018-02-10bb').group(1))
# print(p3.match('2018-02-10').groups())

# year, month, day = p3.match('2018-02-10').groups()
# print(year)

# 4、搜索
# print(p3.search('aa2018-02-10bb'))
# findall()

# 5、替换 (规则、要替换为、代替换)
phone = '123-456-789 # 这是电话号码'
p2 = re.sub(r'#.*$', '', phone)
print(p2)
p3 = re.sub(r'\D', '', p2)
print(p3)
