# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 09:18
# @Author  : sihao
# @File    : 11-归并排序.py
def merge_sort(li,low,high):
    if low<high:#至少有两个元素，递归
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        print(li[low:high+1])


li=[6,3,4,2,9,1,0,5,8]
print(li)
merge_sort(li,0,len(li)-1)
print(li)