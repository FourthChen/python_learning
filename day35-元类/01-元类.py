# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 22:12
# @Author  : sihao
# @File    : 01-元类.py

class StanfordTeacher(object):
    school='Stanford'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s says welcome to the Stanford to learn Python' %self.name)
#所有的对象都是实例化或者说调用类而得到的（调用类的过程称为类的实例化），
# 比如对象t1是调用类StanfordTeacher得到的

t1=StanfordTeacher('lili',18)
print(type(t1)) #查看对象t1的类是<class '__main__.StanfordTeacher'>

'''
如果一切皆为对象，那么类StanfordTeacher本质也是一个对象，
既然所有的对象都是调用类得到的，
那么StanfordTeacher必然也是调用了一个类得到的，这个类称为元类
'''
print(type(StanfordTeacher))
# 结果为<class 'type'>，证明是调用了type这个元类而产生的StanfordTeacher，即默认的元类为type