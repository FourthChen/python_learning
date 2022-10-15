# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 13:15
# @Author  : sihao
# @File    : 6-选择排序.py
def select_sort_simple(li):
    new_li=[]
    for i in range(len(li)):
        min_val=min(li)
        new_li.append(min_val)
        li.remove(min_val)
    return new_li

def select_sort(li):
    for i in range(len(li)-1): #第几趟
        min_loc=i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc=j
        li[i],li[min_loc]=li[min_loc],li[i]
    print(li)

li=[3,2,4,7,1,6,5,8,9]

select_sort(li)