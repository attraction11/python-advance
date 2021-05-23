
# 1、列表推导式一般写法(获取从1到10 所有偶数的平方)：
alist = []
for i in range(1, 11):
    if (i % 2 == 0):
        alist.append(i * i)

print(alist)

# 2、列表推导式优雅写法：
blist = [i * i for i in range(1, 11) if (i % 2) == 0]
print(blist)


zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

# 1、字典推导式一般写法：
z_num_one = {}
for i in zodiac_name:
    z_num_one[i] = 0
print(z_num_one)

# 1、字典推导式一般写法：
z_num_two = {i: 0 for i in zodiac_name}
print(z_num_two)
