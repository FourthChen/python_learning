# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 14:14
# @Author  : sihao
# @File    : 8-快速排序.py
'''
时间复杂度为O(nlogn)
'''
def parition(li,left,right):
    tmp=li[left]
    while left<right:
        while left<right and li[right] >=tmp: #从右面找比tmp小的数
            right-=1 #往左走一步
        li[left]=li[right] #把右边的值放在左边空位上

        while left<right and li[left]<=tmp:
            left+=1  #往右走一步
        li[right]=li[left] #把左边的值放在右边空位上

    li[left]=tmp  #把tmp归位
    return left
def quick_sort(li,left,right):
    if left<right:  #至少两个元素
        mid=parition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)


li=[3,6,1,4,2,5]
print(li)
quick_sort(li,0,len(li)-1)
print(li)