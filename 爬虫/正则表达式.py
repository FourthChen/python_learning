# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 17:51
# @Author  : sihao
# @File    : 正则表达式.py

'''
正则表达式是对字符串操作的一种逻辑公式
'''
# import re
# content='Hello 123 456 World_this is a pig!'
# result=re.match('^Hello\s',content)
# print(result)
# #输出匹配结果
# print(result.group())

#泛匹配
import re
content='Hello 123 456 World_this is a pig!'
result=re.match('^Hello.*pig$',content)
print(result)
#输出匹配结果
print(result.group())
print(result.span())