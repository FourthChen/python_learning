# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 13:01
# @Author  : sihao
# @File    : 24-二叉树.py

"""
二叉树：度不超过2的树

二叉树的链式存储：将二叉树的节点定义为一个对象，节点之间通过类似链表的方式来实现
"""
class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None  #左孩子
        self.rchild=None  #右孩子

a=BiTreeNode('A')
b=BiTreeNode('B')
c=BiTreeNode('C')
d=BiTreeNode('D')
e=BiTreeNode('E')
f=BiTreeNode('F')
g=BiTreeNode('G')

e.lchild=a
e.rchild=g
a.rchild=c
c.lchild=b
c.rchild=d
g.rchild=f

root=e
print(root.lchild.rchild.data)

'''
        E
    A       G
       C       F
   B      D


'''
#前序遍历 EACBDGF

def pre_order(root):
    if root:
        print(root.data,end='')
        pre_order(root.lchild)
        pre_order(root.rchild)

pre_order(root)

#中序遍历 ACBDEGF
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end='')
        in_order(root.rchild)
in_order(root)

#后序遍历 BDCAFGE
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end='')
post_order(root)

#层次遍历，使用队列实现
from collections import deque
def level_order(root):
    queue=deque()
    queue.append(root)
    while len(queue)>0:#只要队不空
        node=queue.popleft()
        print(node.data,end='')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)

level_order(root)