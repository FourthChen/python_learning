# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 12:36
# @Author  : sihao
# @File    : 4-二分查找.py
'''
时间复杂度为O(logn)
'''
def binary_search(li,val):
    left=0
    right=len(li)-1
    while left<=right: #候选区有值
        mid=(left+right)//2
        if li[mid]==val:
            return mid+1
        elif li[mid]>val:
            right=mid-1
        else:
           left=mid+1
    else:
        return None

li=[1,2,3,4,5,6,7,8,9]
print(binary_search(li,1))
