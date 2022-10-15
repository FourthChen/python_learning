# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 21:10
# @Author  : sihao
# @File    : 01-二维数组中的查找.py
"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。

"""
import numpy
def find(target,array):
    rows=len(array)-1
    cols=len(array[0])-1
    i=rows
    j=0
    while j<=cols and i>=0:
        if target<array[i][j]:
            i=i-1
        elif target> array[i][j]:
            j=j+1
        else:
            return True
    return False
def main():
    a=numpy.array(([1,2,3,4],
                  [2,3,4,5],
                  [3,4,5,6],
                  [4,5,6,7]))

    print(a)
    #判断8是否在数组a中
    print(find(8,a))

if __name__=="__main__":
    main()