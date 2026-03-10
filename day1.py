# def chengfa():
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print("%d*%d" % (j, i), end=" ")
#         print()
#
#
# if __name__ == '__main__':
#     chengfa()
# a = [[col * row for col in range(5)] for row in range(5)]
# result = []
# for x in a:
#     for j in x:
#         result.append(j)
# print(result)
# def use_dic():
#     xiaoming_dic = {'name': 'slz'}
#     xiaoming_dic['age'] = 18
#     for k in xiaoming_dic.items():
#         print(k)
import os


# def demo2(num, *args, **kwargs):
#     print(f'demo2{args}')
#     print(f'demo2{kwargs}')
#
#
# def demo(*args, **kwargs):
#     # print(args)
#     # print(kwargs)
#     # print('-' * 50)
#     demo2(args, **kwargs)


# class Person:
#     def __init__(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#
#     def run(self):
#         print(f'{self.name} 正在奔跑')
#
#     def eat(self):
#         print(f'{self.name} 正在吃')


# elephant = Person('大象', 18, 1.75)
# print(elephant.name, elephant.age, elephant.height)
# elephant.eat()
# elephant.run()
# print('-' * 50)
# tiger = Person('老虎', 17, 1.65)
# print(tiger.name, tiger.age, tiger.height)
# tiger.eat()
# tiger.run()
# if __name__ == '__main__':
# use_dic()
# demo(1, 1, 1, 21, name='lyc', age=18, cm=10)


# class Person:
#     def __init__(self, color, variety, name):
#         self.color = color
#         self.variety = variety
#         self.name = name
#         print(f'一只{self.color}色的{self.variety}叫{self.name}')
#
#     def bark(self):
#         print('看见生人汪汪叫')
#
#     def tail(self):
#         print('看见家人摇尾巴')
#
#
# dog = Person('黄', '狗狗', '元宝')
# dog.bark()
# dog.tail()
# class Cat:
#     def __init__(self, new_name):
#         print("这是一个初始化方法")
#         # self.属性名 = 属性的初始值
#         # self.name = "Tom"
#         self.name = new_name
#
#
# def eat(self):
#     print("%s 爱吃鱼" % self.name)
#     # 使用类名()创建对象的时候，会自动调用初始化方法 __init__
#
#
# tom = Cat("Tom")
# print(tom.name)

# class Houseitem:
#     def __init__(self, name, area):
#         '''
#         家具初始化
#         :param name:家具名称
#         :param area: 家具面积
#         '''
#         self.name = name
#         self.area = area

# def __str__(self):
#     return f'{self.name}占地 {self.area}'


#
#
# class House:
#     def __init__(self, house_type, area):
#         """
#         房子初始化
#         :param house_type: 房子类
#         :param area: 占地面积
#         """
#         self.house_type = house_type
#         self.area = area
#         self.free_area = area  # 剩余面积
#         self.item_list = []  # 家具列表
#
#     def __str__(self):
#         return ("户型：%s\n 总面积：%.2f[剩余：%.2f]\n 家具：%s"
#                 % (self.house_type, self.area, self.free_area, self.item_list))
#
#     def add_item(self, item: Houseitem):
#         if item.area > self.free_area:
#             return '房子空间不足，添加失败'
#         self.free_area -= item.area
#         self.item_list.append(item.name)
#
#
# if __name__ == '__main__':
#     bed = Houseitem('席梦思', 100)
#     chest = Houseitem('衣柜', 200)
#     table = Houseitem('餐桌', 300)
#     print(bed)
#     print(chest)
#     print(table)


#     my_home = House('两室一厅', 700)
#     my_home.add_item(bed)
#     my_home.add_item(chest)
#     my_home.add_item(table)
#     print(my_home)
# class Gun:
#     def __init__(self, model):
#         """
#         枪械初始化
#         :param model: 枪类型
#         """
#         self.model = model
#         self.bullet_count = 0
#
#     def add_bullet(self, count):
#         self.bullet_count += count
#
#     def shoot(self):
#         if self.bullet_count <= 0:
#             print('子弹不足，无法开火')
#             return
#         self.bullet_count -= 1
#         print(f'{self.model}发射子弹{self.bullet_count}')
#
#
# class Soldier:
#     def __init__(self, name):
#         """
#         初始化士兵
#         :param name:士兵名字
#         """
#         self.name = name
#         self.gun = None
#
#     def fire(self):
#         if self.gun is None:
#             print(f'{self.name}还没有枪')
#             return
#         print(f'{self.name}冲啊')
#         self.gun.add_bullet(50)
#         self.gun.shoot()
#
#
# class Women:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# class Dog(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
# class Dog(object):
#     def __init__(self, name):
#         self.name = name
#
#     def game(self):
#         print("%s 蹦蹦跳跳的玩耍..." % self.name)
#
#
# class XiaoTianDog(Dog):
#     def game(self):
#         print("%s 飞到天上去玩耍..." % self.name)
#
#
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def game_with_dog(self, dog):
#         print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
#         # 让狗玩耍
#         dog.game()
#
#
# # 1. 创建一个狗对象
# wangcai1 = Dog("旺财")
# wangcai2 = XiaoTianDog("飞天旺财")
# # 2. 创建一个大象对象
# xiaoming = Person("大象")
# xiaoming.game_with_dog(wangcai1)
# xiaoming.game_with_dog(wangcai2)
# if __name__ == '__main__':
# xusanduo = Soldier('许三多')
# xusanduo.fire()
# print('-' * 50)
# ak47 = Gun('ak47')
# xusanduo.gun = ak47
# xusanduo.fire()
# xiaohong = Women('小红', 20)
# print(xiaohong.name)
# print(xiaohong.age)
# while True:
#     try:
#         num = int(input('请输入一个数字'))
#         print(int(num))
#         break
#     except:
#         print('输入必须为数字')
# while True:
#     try:
#         num = int(input("请输入整数："))
#         result = 8 / num
#         print(result)
#         break
#     except ValueError:
#         print("请输入正确的整数")
#     except ZeroDivisionError:
#         print("除 0 错误")
# def input_password():
#     pwd = input("请输入密码：")
#     if len(pwd) >= 8:
#         return pwd
#     ex = Exception("密码长度不够")
#     raise ex


#
# try:
#     print(input_password())
# except Exception as result:
#     print(result)
# try:
#     assert 1 == 0, "你的程序在这里发生了什么什么错误"
# except Exception as e:
#     print(e)
# def use_file():
#     file = open('test1', 'w+', encoding='utf-8')
#     file.write('你是谁')
#     file.seek(3, os.SEEK_SET)
#     data = file.read()
#     print(data)
#     file.close()
def scan_dir(current_path, width):
    file_list = os.listdir(current_path)
    for file in file_list:
        print(' ' * width, file)
        if os.path.isdir(file):
            scan_dir(file, width + 4)


if __name__ == '__main__':
    scan_dir(os.getcwd(), 0)
# def test():
#     x = int(input("请输入一个数："))
#     assert x > 0, '请输入大于零的数'
#     print(x)


# if __name__ == '__main__':
# while True:
#     try:
#         test()
#     except Exception as e:
#         print(e)
# test()
