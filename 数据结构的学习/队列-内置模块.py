# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 09:15
# @Author  : sihao
# @File    : 队列-内置模块.py
'''
双向队列
    两头都能进出
'''
from collections import deque
q=deque([1,2,3])
q.append(4) #队尾进队
print(q.popleft()) #队首出队
#双向队列
# # q.appendleft(1)#队首进队
# # q.pop()#队尾出队
#