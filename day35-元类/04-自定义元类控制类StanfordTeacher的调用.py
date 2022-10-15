# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 08:39
# @Author  : sihao
# @File    : 04-自定义元类控制类StanfordTeacher的调用.py

'''
所有的函数都是可调用对象。
一个类实例也可以变成一个可调用对象，
只需要实现一个特殊方法__call__
'''
class Foo:
    def __call__(self, *args, **kwargs):
        print(self)
        print(args)
        print(kwargs)

obj=Foo()
#1、要想让obj这个对象变成一个可调用的对象，需要在该对象的类中定义一个方法__call__方法，该方法会在调用对象时自动触发
#2、调用obj的返回值就是__call__方法的返回值
res=obj(1,2,3,x=1,y=2)

'''
调用一个对象，
就是触发对象所在类中的__call__方法的执行，
如果把StanfordTeacher也当做一个对象，
那么在StanfordTeacher这个对象的类中也必然存在一个__call__方法
'''
class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __call__(self, *args, **kwargs):
        print(self) #<class '__main__.StanfordTeacher'>
        print(args) #('lili', 18)
        print(kwargs) #{}
        return 123

class StanfordTeacher(object,metaclass=Mymeta):
    school='Stanford'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s says welcome to the Stanford to learn Python' %self.name)



# 调用StanfordTeacher就是在调用StanfordTeacher类中的__call__方法
# 然后将StanfordTeacher传给self,溢出的位置参数传给*，溢出的关键字参数传给**
# 调用StanfordTeacher的返回值就是调用__call__的返回值
t1=StanfordTeacher('lili',18)
print(t1) #123