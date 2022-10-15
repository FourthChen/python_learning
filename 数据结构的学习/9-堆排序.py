# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 07:46
# @Author  : sihao
# @File    : 9-堆排序.py
'''
时间复杂度是O(nlogn)
'''
def sift(li,low,high):
    '''

    :param li:  列表
    :param low:  堆的根节点位置
    :param high:  堆的最后一个元素的位置
    :return:
    '''
    i=low
    j=2*i+1 #j开始是左孩子
    tmp=li[low] #把堆顶存起来
    while j<=high: #只要j位置有数
        if j+1<=high and li[j+1]>li[j]:
            j=j+1 #j指向右孩子
        if li[j]>tmp:
            li[i]=li[j]
            i=j #往下看一层
            j=2*i+1
        else:  #tmp大，把tmp放在l[i]
            li[i]=tmp #把tmp放在某一级的位置上
            break
    else:
        li[i]=tmp  #把tmp放在叶子节点上


def heap_sort(li):
    n=len(li)
    for i in range((n-2)//2,-1,-1):
        #i代表建堆时候调整的部分的根的下标
        sift(li,i,n-1)
    #堆就建完了
    for i in range(n-1,-1,-1):
        #i 指向当前堆的最后一个元素
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1)
li=[i for i in range(10)]
import random
random.shuffle(li)
print(li)
heap_sort(li)
print(li)