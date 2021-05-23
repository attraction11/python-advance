######################## 1、变量用法: ########################
# 输出一行文字
# print('hello world!')

######################## 2、变量用法: ########################

# 网络带宽计算
# bandwidth = 100
# ratio = 8
# print(bandwidth / ratio)

######################## 3、序列用法: ########################

# 记录生肖，根据年份判断生肖
# chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])
# year = 2018
# print(year % 12)
# print(chinese_zodiac[year % 12])

###### 序列-字符串 ######

# # 切片操作符([:])                序列[0:整数]
# print(chinese_zodiac[0:4])
# # 重复操作符(*)                  序列*整数
# print(chinese_zodiac * 3)
# # 连接操作符(+)                  序列+序列
# print(chinese_zodiac + '猫')
# # 成员关系操作符(in、not in)     对象[not] in序列
# print('狗' in chinese_zodiac)

###### 序列-元组 ######

# 元组嵌套，元组存储的内容不可变更
# zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
#                u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
# (month, day) = (12, 13)
# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# # print(list(zodiac_day))
# zodiac_len = len(list(zodiac_day)) % 12
# print(zodiac_name[zodiac_len])

###### 序列-列表 ######

# 列表同字符串，有：切片操作符([:])、重复操作符(*)、连接操作符(+)、成员关系操作符(in、not in)
# a_list = ['abc', 'xyz']
# a_list.append('X')
# print(a_list)
# a_list.remove('xyz')
# print(a_list)

######################## 4、条件与循环 #######################

###### 条件语句 ######

# x = 'xyz'
# if x == 'abc':
#     print('x值与abc相等')
# elif x == 'xyz':
#     print('x值与xyz不相等')
# else:
#     print('x值...')
# chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# year = int(input('请用户输入出生年份'))
# if chinese_zodiac[year % 12] == '狗':
#     print('狗年运势....')

###### for循环语句 ######

# for cz in chinese_zodiac:
#     print(cz)
# for i in range(1, 13):
#     print(i)
# for year in range(2000, 2021):
#     print('%s 年的生肖是 %s' %(year, chinese_zodiac[year % 12]))

###### while循环语句 ######

# import time
# num = 5
# while True:
#     num = num + 1
#     if num == 10:
#         continue
#     print(num)
#     time.sleep(1)

# zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
#                u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# int_month = int(input('请输入月份'))
# int_day = int(input('请输入日期'))

# print(type(int_month))
# for zd_num in range(len(zodiac_days)):
#     if zodiac_days[zd_num] >= (int_month, int_day):
#         print(zodiac_name[zd_num])
#         break
#     elif int_month == 12 and int_day > 23:
#         print(zodiac_name[0])
#         break

# n = 0
# while zodiac_days[n] < (int_month, int_day):
#     if int_month == 12 and int_day > 23:
#         break
#     n += 1
# print(zodiac_name[n])

######################## 5、映射与字典 #######################
dict1 = {}
print(type(dict1))
dict2 = {'x': 1, 'y': 2}
dict2['z'] = 3
print(dict2)