# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 19:20
# @Author  : sihao
# @File    : 02-re模块.py
'''
正则就是用一些具有特殊含义的符号组合到一起（称为正则表达式）
来描述字符或者字符串的方法。或者说：正则就是用来描述一类事物的规则。
'''
import re
print(re.findall('\w','abc123_*()-='))
print(re.findall('\W','abc123_*()-= '))

print(re.findall('\s','\ra\fb\c123_*()-='))
print(re.findall('\S','\ra\fb\c123_*()-='))

print(re.findall('\d','\ra\fb\c123_*()-='))