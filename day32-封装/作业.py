# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 22:11
# @Author  : sihao
# @File    : 作业.py
class school:
    school_name='oldboy'

    def __init__(self,nickname,addr):
        self.nickname=nickname
        self.addr=addr
        self.classes=[]
    def related(self,Class):
        self.classes.append(Class)

    def tell_class(self):
        print(self.nickname.center(60,'='))
        for i in self.classes:
            i.tellcourse()

#一。学校
#1.创建校区
school_obj1=school('上海校区','上海')
school_obj2=school('北京校区','北京')

#2.为学校开设班级
school_obj1.related('脱产14期')
school_obj1.related('脱产15期')


school_obj2.related('28期')
school_obj2.related('脱产29期')

#3.查看每个校区开设的班级
# school_obj1.tell_class()
# school_obj2.tell_class()

class Class:
    def __init__(self,name):
        self.name=name
        self.course=None
    def related_course(self,course_name):
        self.course=course_name
    def tell_course(self):
        print('%s %s '%(self.name,self.course))
#二。班级
#1.创建班级
class_obj1=Class('脱产14期')
class_obj2=Class('脱产15期')
class_obj3=Class('脱产29期')

#2.为班级关联一个课程
class_obj1.related_course('python全栈开发')
class_obj2.related_course('linux 运维')
class_obj3.related_course('python全栈开发')
#3.查看班级开设的课程信息
class_obj1.tell_course()
class_obj2.tell_course()

#4.为学校开设班级
school_obj1.related(class_obj1)
school_obj1.related(class_obj2)

school_obj1.tell_class()
school_obj2.tell_class()


school_obj2.related(class_obj3)
class course:
    pass

class stu:
    pass