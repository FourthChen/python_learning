# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 19:07
# @Author  : sihao
# @File    : 18-队列.py
'''
队列是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除
进行插入的一端是队尾，记为进队或入队
进行删除的一端为对头，记为出队
先进先出

队列的实现方式------环形队列
'''
class Queue:
    def __init__(self,size):
        self.queue=[0 for _ in range(size)]
        self.size=size
        self.rear=0 #队尾指针
        self.front=0 #队首指针
    def push(self,element):
        if not self.is_filled():
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
        else:
            return None

    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            return None
    #判断队空
    def is_empty(self):
        return self.rear==self.front
    #判断队满
    def is_filled(self):
        return (self.rear+1)%self.size==self.front

q=Queue(5)
for i in range(4):
    q.push(i)

print(q.pop())
print(q.is_filled())
q.push(4)
print(q.is_filled())