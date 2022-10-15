# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 12:59
# @Author  : sihao
# @File    : 5-冒泡排序.py

'''
算法复杂度为O(n^2)
'''
import random
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]<li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]


li=[4,2,1,7,5,3,9,6,8]
print(li)
bubble_sort(li)
print(li)

'''
改进的冒泡排序
若其中一趟排序没有发生交换，则说明列表已经有序
可以直接结束算法
'''
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-i-1):
            if li[j]<li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        if not exchange:
            return
