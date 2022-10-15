# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 21:49
# @Author  : sihao
# @File    : 01.py

class stu:
    school='清华大学'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def tell_info(self):
        print(self.name,self.age,self.gender)

    def choose(self):
        print('%s is choosing a course'%self.name)


obj=stu('alex',10,'male')
obj.tell_info()
print(stu.__dict__)
print(obj.__dict__)

#1.类中的数据属性
print(stu.school)
#2.类中的函数属性
print(stu.choose)