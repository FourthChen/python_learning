# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 21:29
# @Author  : sihao
# @File    : 绑定方法.py
'''
类中定义的函数分为两大类：绑定方法和非绑定方法

​其中绑定方法又分为绑定到对象的对象方法和绑定到类的类方法。

​在类中正常定义的函数默认是绑定到对象的，
而为某个函数加上装饰器@classmethod后，该函数就绑定到了类。
'''
HOST='127.0.0.1'
PORT=3306

# 类方法的应用
import settings
class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port
    @classmethod
    def from_conf(cls): # 从配置文件中读取配置进行初始化
        return cls(settings.HOST,settings.PORT)
print(MySQL.from_conf)  #绑定到类的方法
conn=MySQL.from_conf() # 调用类方法，自动将类MySQL当作第一个参数传给cls
print(conn)