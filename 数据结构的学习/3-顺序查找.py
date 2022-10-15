# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 12:24
# @Author  : sihao
# @File    : 3-顺序查找.py

'''
时间复杂度是O(n)
'''
def liner_search(li,val):
    #enumerate()用于可迭代\可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标.
    for ind,v in enumerate(li):
        if v==val:
            return ind
    else:
        return None