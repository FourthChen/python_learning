# class base:
#     def login(self):
#         raise NotImplementedError("没有实现login方法")
#     def kantie(self):
#         raise NotImplementedError("没有实现kantie方法")
# #张三
# class normal(base):
#     def login(self):
#         print("普通人登录")
#
# #李四
# class member(base):
#     def login(self):
#         print("吧务登录")
#
# #王五
# class admin(base):
#     def login(self):
#         print("管理员登录")
#
# def login(obj):
#     print("开始验证")
#     print("进入主页")
#
# n=normal()
# m=member()
# a=admin()
#
# login(n)
# login(m)
# login(a)
#
# #重写：子类对父类提供的方法进行改写

from abc import ABCMeta, abstractclassmethod

class animal(metaclass=ABCMeta):  #在父类中写metaclass=xxx  抽象类，类中存在抽象方法，类一定时抽象类
    @abstractclassmethod  #抽象方法
    def chi(self):  #抽象的概念
        pass
    def dong(self):
        print("蠕动")

class cat(animal): #子类必须实现父类中的抽象方法
    def chi(self): #具体的实现
        print("猫爱吃鱼")

