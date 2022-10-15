# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 11:52
# @Author  : sihao
# @File    : 2-汉诺塔问题.py
max=0
def hanoi(n,a,b,c):
    #统计移动的次数
    global max
    if n>0:
        max = max + 1
        hanoi(n-1,a,c,b)
        print("moving from %s to %s"%(a,c))
        hanoi(n-1,b,a,c)


hanoi(4,'A','B','C')
print("一共移动了%s次"%max)