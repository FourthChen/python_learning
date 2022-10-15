# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 08:21
# @Author  : sihao
# @File    : 03-自定义元类控制类StanfordTeacher的创建.py

'''
一个类没有声明自己的元类，
默认他的元类就是type，除了使用内置元类type，
我们也可以通过继承type来自定义元类，
然后使用metaclass关键字参数为一个类指定元类
'''

class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    pass

# StanfordTeacher=Mymeta('StanfordTeacher',(object),{...})
class StanfordTeacher(object,metaclass=Mymeta):
    school='Stanford'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s says welcome to the Stanford to learn Python' %self.name)


'''
自定义元类可以控制类的产生过程，
类的产生过程其实就是元类的调用过程,
即StanfordTeacher=Mymeta('StanfordTeacher',(object),{...})，
调用Mymeta会先产生一个空对象StanfordTeacher，
然后连同调用Mymeta括号内的参数一同传给Mymeta下的__init__方法，完成初始化，
'''
class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __init__(self,class_name,class_bases,class_dic):
        # print(self) #<class '__main__.StanfordTeacher'>
        # print(class_bases) #(<class 'object'>,)
        # print(class_dic) #{'__module__': '__main__', '__qualname__': 'StanfordTeacher', 'school': 'Stanford', '__init__': <function StanfordTeacher.__init__ at 0x102b95ae8>, 'say': <function StanfordTeacher.say at 0x10621c6a8>}
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类的功能

        if class_name.islower():
            raise TypeError('类名%s请修改为驼峰体' %class_name)

        if '__doc__' not in class_dic or len(class_dic['__doc__'].strip(' \n')) == 0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')

# StanfordTeacher=Mymeta('StanfordTeacher',(object),{...})
class StanfordTeacher(object,metaclass=Mymeta):
    """
    类StanfordTeacher的文档注释
    """
    school='Stanford'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s says welcome to the Stanford to learn Python' %self.name)