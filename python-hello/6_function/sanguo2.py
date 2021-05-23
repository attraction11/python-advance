import re

# 获取文件中某个主角的出现次数


def find_item(hero):
    with open('sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        # print('主角 %s 出现 %s 次' % (hero, len(name_num)))
    return len(name_num)


# 读取人物信息
name_dict = {}
with open('name.txt', encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num

# 根据人物出现的次数排序
name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0: 10])

