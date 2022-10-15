# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 22:58
# @Author  : sihao
# @File    : 01-多态.py

#多态指的是一类事物有多种形态，比如动物有多种形态：猫、狗、猪
'''
class Animal: #同一类事物:动物
    def talk(self):
        pass
class Cat(Animal): #动物的形态之一:猫
    def talk(self):
        print('喵喵喵')
class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('汪汪汪')
class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('哼哼哼')

#实例化得到三个对象
cat=Cat()
dog=Dog()
pig=Pig()
'''

'''
多态性指的是可以在不用考虑对象具体类型的情况下而直接使用对象，
这就需要在设计时，把对象的使用方法统一成一种：
例如cat、dog、pig都是动物,但凡是动物肯定有talk方法，
于是我们可以不用考虑它们三者的具体是什么类型的动物,而直接使用
'''
def Talk(animal):
    animal.talk()

'''
多态性的好处在于增强了程序的灵活性和可扩展性，
比如通过继承Animal类创建了一个新的类，实例化得到的对象obj，
可以使用相同的方式使用obj.talk()
'''

# print(Talk(cat))
# print(Talk(dog))
# print(Talk(pig))

'''
多态性的本质在于不同的类中定义有相同的方法名，
这样我们就可以不考虑类而统一用一种方式去使用对象，
可以通过在父类引入抽象类的概念来硬性限制子类必须有某些方法名
'''

'''
class wolf(Animal):
    def talk(self):
        print('┗|｀O′|┛ 嗷~~')

wolf=wolf()
wolf.talk()
'''
import abc

# 指定metaclass属性将类设置为抽象类，抽象类本身只是用来约束子类的，不能被实例化
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod # 该装饰器限制子类必须定义有一个名为talk的方法
    def talk(self): # 抽象方法中无需实现具体的功能
        print('animal.talk')

class Cat(Animal): # 但凡继承Animal的子类都必须遵循Animal规定的标准
    def talk(self):
        print('cat.talk')

cat=Cat() # 若子类中没有一个名为talk的方法则会抛出异常TypeError，无法实例化
print(cat.talk())

'''
Python崇尚的“鸭子类型”（duck typing）：
“如果看起来像、叫声像而且走起路来像鸭子，那么它就是鸭子”。
比起继承的方式，鸭子类型在某种程度上实现了程序的松耦合度
'''
#二者看起来都像文件,因而就可以当文件一样去用，然而它们并没有直接的关系
class Txt: #Txt类有两个与文件类型同名的方法，即read和write
    def read(self):
        pass
    def write(self):
        pass

class Disk: #Disk类也有两个与文件类型同名的方法：read和write
    def read(self):
        pass
    def write(self):
        pass