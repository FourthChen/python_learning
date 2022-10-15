# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 18:34
# @Author  : sihao
# @File    : 02-实现面向对象编程.py

#先定义类

#在调用类产生对象

#类是对象相似数据与功能的集合体
#注意：类体代码是在类定义阶段就会立即执行
#1.定义类
class stu:
    #1.变量的定义
    stu_name="old"

    def __init__(self,name):
        self.stu_name=name
        print("我是%s"%self.stu_name)
        print("---------")

    # 2.功能的定义
    def tell_stu_info(self):
        print("!!!")

    print("======")
#2.再调用类产生对象
#调用类的过程又称为实例化，发生了三件事
    '''
    1.先产生了一个空对象
    2.python自动调用类中的__init__()方法，然后将空对象已经调用类时括号内传入的参数一同传递给__init__方法
    3.返回初始完的对象
    '''
stu_obj1=stu('aaa')

#总结__init__方法
#1.会调用类时自动触发执行，用来为对象初始化自己独有的数据
#2.__init__内应该存放是为对象初始化属性的功能，但是可以存放任意其他代码
#3.__init__方法必须返回None
