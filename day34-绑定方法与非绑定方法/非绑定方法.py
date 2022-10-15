# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 21:46
# @Author  : sihao
# @File    : 非绑定方法.py
'''
为类中某个函数加上装饰器@staticmethod后，
该函数就变成了非绑定方法，也称为静态方法。
该方法不与类或对象绑定，类与对象都可以来调用它，
但它就是一个普通函数而已，因而没有自动传值那么一说
'''
import uuid
class MySQL:
    def __init__(self,host,port):
        self.id=self.create_id()
        self.host=host
        self.port=port
    @staticmethod
    def create_id():
        return uuid.uuid1()

conn=MySQL('127.0.0.1',3306)
print(conn.id)
print(MySQL.create_id)
print(conn.create_id)
'''
总结绑定方法与非绑定方法的使用：
若类中需要一个功能，该功能的实现代码中需要引用对象则将其定义成对象方法、
需要引用类则将其定义成类方法、
无需引用类或对象则将其定义成静态方法。
'''