# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 08:56
# @Author  : sihao
# @File    : 04-property属性.py
'''
property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值
'''
''' 
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight / (self.height**2)

p1=People('egon',69,1.70)
print(p1.bmi)
'''

''' 
import math
class Circle:
    def __init__(self,radius): #圆的半径radius
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2 #计算面积

    @property
    def perimeter(self):
        return 2*math.pi*self.radius #计算周长

c=Circle(10)
print(c.radius)
print(c.area) #可以向访问数据属性一样去访问area,会触发一个函数的执行,动态计算出一个值
print(c.perimeter) #同上
#此时的特性area和perimeter不能被赋值
'''

'''
一个静态属性property本质就是实现了get，set，delete三种方法
'''
class Foo:
    @property
    def AAA(self):
        print('get的时候运行我啊')

    @AAA.setter
    def AAA(self,value):
        print('set的时候运行我啊')

    @AAA.deleter
    def AAA(self):
        print('delete的时候运行我啊')

#只有在属性AAA定义property后才能定义AAA.setter,AAA.deleter
f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA

'''
class Foo:
    def get_AAA(self):
        print('get的时候运行我啊')

    def set_AAA(self,value):
        print('set的时候运行我啊')

    def delete_AAA(self):
        print('delete的时候运行我啊')
    AAA=property(get_AAA,set_AAA,delete_AAA) #内置property三个参数与get,set,delete一一对应

f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA
'''

'''
class Goods:

    def __init__(self):
        # 原价
        self.__original_price = 100
        # 折扣
        self.__discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.__original_price * self.__discount
        return new_price

    @price.setter
    def price(self, value):
        self.__original_price = value

    @price.deleter
    def price(self):
        del self.__original_price


obj = Goods()
print(obj.price)         # 获取商品价格
obj.price = 200   # 修改商品原价
print(obj.price)
del obj.price     # 删除商品原价

'''
#classmethod方法
class Classmethod_Demo():
    role = 'dog'

    @classmethod
    def func(cls):
        print(cls.role)

Classmethod_Demo.func()

#staticmethod方法
class Staticmethod_Demo():
    role = 'dog'

    @staticmethod
    def func():
        print("当普通方法用")

Staticmethod_Demo.func()  #打印不出来dog

#作业
class Foo:
    def func(self):
        print('in father')


class Son(Foo):
    def func(self):
        print('in son')

s = Son()
s.func()
# 请说出上面一段代码的输出并解释原因？