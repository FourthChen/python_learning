# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 11:46
# @Author  : sihao
# @File    : 28-背包问题.py
"""
背包问题
    一个小偷发现n个商品，第i个商品价值Vi元，重Wi千克。他希望拿走的价值尽量高
    但背包只能容纳W千克的东西，那他应该拿走哪些商品？

0-1背包：对于一个商品，小偷要么完整拿走，要么留下。不能拿一部分，或一个商品拿走多次。(商品为金条)

分数背包：对于一个商品，小偷可以拿走其中任意一部分（商品为金砂）
"""
goods=[(60,10),(100,20),(120,30)]  #（价格，重量）
goods.sort(key=lambda x:x[0]/x[1],reverse=True)

def fractional_backpack(goods,w):
    m=[0 for _ in range(len(goods))]
    for i,(prize,weight)in enumerate(goods):
        if w>=weight:
            m[i]=1
            w-=weight
        else:
            m[i]=w/weight
            w=0
            break
    return m

print(fractional_backpack(goods,50))