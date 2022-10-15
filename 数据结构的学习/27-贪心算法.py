# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 09:42
# @Author  : sihao
# @File    : 27-贪心算法.py
'''
贪心算法是指，在问题求解时，总是做出在当前看来是最好的选择
'''

'''
找零问题
    假设老板需要找零n元钱，钱币的面额有：100元，50元，20元，五元，一元
    如何找零使得所需钱币的数量最少？

'''
t=[100,50,20,5,1]
def change(t,n):
    m=[0 for _ in range(len(t))]  #全为0
    for i,money in enumerate(t):
        m[i]=n//money
        n=n%money

    return m,n

print(change(t,89))