# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 08:05
# @Author  : sihao
# @File    : 03-封装.py
'''
封装：是指隐藏对象的属性和实现细节，仅对外提供公共访问方式。

好处：将变化隔离、便于使用、提高重用性、提高安全性

封装原则：将不需要对外提供的内容都隐藏起来、把属性都隐藏，提供公共方法对其访问。

'''
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.age = score
#
# alex=Student("alex",12)
# yuan=Student("yuan",34)
#
#
# alex.age=1000
# print(alex.age)

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__age = score
#
# alex=Student("alex",12)
# yuan=Student("yuan",34)
# #已经无法从外部访问实例变量.__name和实例变量.__score了
# print(alex.__age)


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__age = score
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
#但是如果外部代码要获取name和score怎么办？
# 可以给Student类增加get_name和get_score这样的方法
alex=Student("alex",12)
yuan=Student("yuan",34)

print(alex.get_age())

#如果又要允许外部代码修改age怎么办？
# 可以再给Student类增加set_age方法

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__age = score

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age

alex=Student("alex",12)
print(alex.get_age())
alex.set_age(1000)
print(alex.get_age())
'''
在Python中，变量名类似__xxx__的，也就是以双下划线开头，
并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，
不是private变量，所以，不能用__name__、__score__这样的变量名。
'''
'''

    __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。

    _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问。不限语法）

    __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

'''
class a:
    def fa(self):
        print('from a')
    def test(self):
        self.fa()
#b继承a
class b(a):
    def fa(self):
        print('from b')

b1=b()
b1.test()
#在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
class a:
    # 在定义时就变形为_a__fa
    def __fa(self):
        print('from a')

    def test(self):
        #只会与自己所在的类为准, 即调用_a__fa
        self.__fa()


# b继承a
class b(a):
    def fa(self):
        print('from b')


b1 = b()
b1.test()