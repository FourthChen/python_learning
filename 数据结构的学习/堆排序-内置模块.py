# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 13:44
# @Author  : sihao
# @File    : 堆排序-内置模块.py
import heapq

import random
li=list(range(20))

random.shuffle(li)
print(li)


heapq.heapify(li)#建堆
heapq.heappop(li)