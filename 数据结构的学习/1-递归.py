# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 11:45
# @Author  : sihao
# @File    : 1-递归.py

def func3(x):
    if x>0:
        print(x)
        func3(x-1)


def func4(x):
    if x > 0:
        func4(x - 1)
        print(x)

func3(4)
print('=====================')
func4(4)