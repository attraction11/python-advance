# 1、面向过程编程
# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
# def print_role(rolename):
#     print('name is %s, hp is %s' % (rolename['name'], rolename['hp']))

# print_role(user1)

# user1 = Player('tom', 100, 'war')
# user2 = Player('jerry', 90, 'master')
# user1.print_role()
# user2.print_role()
# user1.updateName('wilson')
# user1.print_role()
# user1.__name = 'aaaa' # 修改失败
# user1.print_role()

# 2、面向对象编程:  
# 特征点: 封装(定义私有属性或方法)、继承、多态(运行时多种状态)
# 类是描述具有相同属性和方法的集合
class Player():
    def __init__(self, name, hp, occu):
        # 添加__后的属性只能通过方法修改，不能直接赋值修改
        self.__name = name   # 变量被称为属性
        self.hp = hp
        self.occu = occu

    def print_role(self):  # 定义方法
        print('%s: %s %s' % (self.__name, self.hp, self.occu))

    def updateName(self, newName):
        self.name = newName


class Monster():
    '定义怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物')
    pass


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        super().__init__(hp)
    pass


class Boss(Monster):
    'Boss类怪物'
    def __init__(self, hp=1000):
        self.hp = hp

    def whoami(self):
        print('我是怪物我怕谁')
    pass


a1 = Monster(200)
print(a1.hp)
print(a1.run())

a2 = Animals(1)
print(a2.hp)
print(a2.run())

a3 = Boss(800)
a3.whoami()

print('a1的类型%s' % type(a1))
print('a2的类型%s' % type(a2))
print('a3的类型%s' % type(a3))

print(isinstance(a2, Monster))
print(isinstance('str', object))
print(isinstance(123, object))