# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 12:12
# @Author  : sihao
# @File    : 29-数字拼接.py
'''
拼接最大数字问题
    有n个非负整数，按照字符串拼接的方式拼接为一个整数。
    如何使得拼接的最大？

例如：32，65，87可以拼接的最大整数为
876523
'''
from functools import cmp_to_key

li=[32,94,128,1286,6,71]
def xy_cmp(x,y):
    if x+y<y+x:
        return 1
    elif x+y>y+x:
        return -1
    else:
        return 0
print(li)
def number_join(li):
    li=list(map(str,li))
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)
print(number_join(li))
