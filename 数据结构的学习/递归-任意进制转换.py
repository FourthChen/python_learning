# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 10:38
# @Author  : sihao
# @File    : 递归-任意进制转换.py

def tostr(n,base):
    converString="0123456789ABCDEF"
    if n<base:
        return converString[n]
    else:
        return tostr(n//base,base)+converString[n%base]

print(tostr(2134,2))