# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 13:44
# @Author  : sihao
# @File    : 7-插入排序.py
'''
时间复杂度为O(n^2)
'''
def insert_sort(li):
    for i in range(1,len(li)): #表示摸到的牌的下标
        tmp=li[i]
        j=i-1 #j是手里的牌的下标
        while j>=0 and li[j]>tmp:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tmp
        print(li)

li=[3,6,1,4,2,5]
print(li)
insert_sort(li)
# print(li)