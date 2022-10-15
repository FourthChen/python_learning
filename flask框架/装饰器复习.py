# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:56
# @Author  : sihao
# @File    : 装饰器复习.py

def war(func):
    def inner(*args,**kwargs):
        a2=args[0]*2
        ret=func(a2)
        return ret
    return inner
@war   #inner=war(f=func)
def func(a):
    print(a)
    return a


func(2)