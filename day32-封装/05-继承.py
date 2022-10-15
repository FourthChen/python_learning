# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 21:39
# @Author  : sihao
# @File    : 05-继承.py
'''
继承是一种创建新类的方式，
在Python中，新建的类可以继承一个或多个父类，
新建的类可称为子类或派生类，父类又可称为基类或超类

'''
class ParentClass1: #定义父类
    pass

class ParentClass2: #定义父类
    pass

class SubClass1(ParentClass1): #单继承
    pass

class SubClass2(ParentClass1,ParentClass2): #多继承
    pass

#通过类的内置属性__bases__可以查看类继承的所有父类
print(SubClass1.__bases__)
print(SubClass2.__bases__)


class People:
    school='清华大学'

    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

class Student(People):
    def choose(self):
        print('%s is choosing a course' %self.name)

class Teacher(People):
    def teach(self):
        print('%s is teaching' %self.name)


teacher1=Teacher('lili','male',18)
print(teacher1.name,teacher1.sex,teacher1.age)

'''
有了继承关系，对象在查找属性时，先从对象自己的__dict__中找，
如果没有则去子类中找，然后再去父类中找…… 
'''
class foo:
    def f1(self):
        print('foo.f1')
    def f2(self):
        print('foo.f2')
        self.f1()

class bar(foo):
    def f1(self):
        print('bar.f1')

b=bar()
b.f2()

'''
b.f2()会在父类Foo中找到f2，
先打印Foo.f2,然后执行到self.f1(),即b.f1()，
仍会按照：对象本身->类Bar->父类Foo的顺序依次找下去，
在类Bar中找到f1，因而打印结果为bar.f1
'''

#父类如果不想让子类覆盖自己的方法，可以采用双下划线开头的方式将方法设置为私有的
class foo:
    def __f1(self): # 变形为_Foo__f1
        print('foo.f1')
    def f2(self):
        print('foo.f2')
        self.__f1() # 变形为self._Foo__f1,因而只会调用自己所在的类中的方法

class bar(foo):
    def __f1(self): # 变形为_Bar__f1
        print('bar.f1')

b=bar()
b.f2()

#继承的菱形问题
class A(object):
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B,C):
    pass


obj = D()
print(D.mro()) # 新式类内置了mro方法可以查看线性列表的内容，经典类没有该内置该方法
obj.test() # 结果为：from B
'''
1.子类会先于父类被检查
2.多个父类会根据它们在列表中的顺序被检查
3.如果对下一个类存在两个合法的选择,选择第一个父类
'''

'''
Mixins机制指的是子类混合(mixin)不同类的功能，
而这些类采用统一的命名规范（例如Mixin后缀），
以此标识这些类只是用来混合功能的，并不是用来标识子类的从属"is-a"关系的，
所以Mixins机制本质仍是多继承，
这个类是作为功能添加到子类中，而不是作为父类，它的作用同Java中的接口。
但同样遵守”is-a”关系，如下:
'''

#子类可以派生出自己新的属性，在进行属性查找时，子类中的属性名会优先于父类被查找，
class People:
    school='清华大学'

    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

class Teacher(People):
    def __init__(self,name,sex,age,title): #派生
        self.name=name
        self.sex=sex
        self.age=age
        self.title=title
    def teach(self):
        print('%s is teaching' %self.name)


teacher1=Teacher('lili','male',18,'讲师')#只会找自己类中的__init__，并不会自动调用父类的
print(teacher1.name,teacher1.sex,teacher1.age)


#调用super()会得到一个特殊的对象，该对象专门用来引用父类的属性，且严格按照MRO规定的顺序向后查找
class Teacher(People):
    def __init__(self,name,sex,age,title): #派生
        super.__init__(name,sex,age)
        self.title=title
    def teach(self):
        print('%s is teaching' %self.name)


'''
组合
在一个类中以另外一个类的对象作为数据属性，称为类的组合。
组合与继承都是用来解决代码的重用性问题。
不同的是：继承是一种“是”，当类之间有很多相同的之处，应该使用继承；
而组合则是一种“有”的关系，当类之间有显著不同，并且较小的类是较大的类所需要的组件时，应该使用组合
'''
class Course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<%s %s %s>' %(self.name,self.period,self.price))

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def tell_birth(self):
       print('<%s-%s-%s>' %(self.year,self.mon,self.day))

class People:
    school='清华大学'
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

#Teacher类基于继承来重用People的代码，基于组合来重用Date类和Course类的代码
class Teacher(People): #老师是人
    def __init__(self,name,sex,age,title,year,mon,day):
        super().__init__(name,age,sex)
        self.birth=Date(year,mon,day) #老师有生日
        self.courses=[] #老师有课程，可以在实例化后，往该列表中添加Course类的对象
    def teach(self):
        print('%s is teaching' %self.name)


python=Course('python','3mons',3000.0)
linux=Course('linux','5mons',5000.0)
teacher1=Teacher('lili','female',28,'博士生导师',1990,3,23)

# teacher1有两门课程
teacher1.courses.append(python)
teacher1.courses.append(linux)

# 重用Date类的功能
teacher1.birth.tell_birth()

# 重用Course类的功能
for obj in teacher1.courses:
    obj.tell_info()

#此时对象teacher1集对象独有的属性、Teacher类中的内容、Course类中的内容于一身（都可以访问到），是一个高度整合的产物