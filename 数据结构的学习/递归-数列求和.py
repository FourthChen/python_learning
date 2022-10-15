# -*- coding: utf-8 -*-
# @Time    : 2020/7/12 10:14
# @Author  : sihao
# @File    : 递归-数列求和.py
'''
递归是调用自身
    把数组求和转化为“首个数”+“余下数列‘的和
'''
def listnum(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        return numlist[0]+listnum(numlist[1:])

print(listnum([1,2,3]))