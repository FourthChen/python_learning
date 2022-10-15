# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 08:44
# @Author  : sihao
# @File    : 22-哈希表.py
'''
哈希表
    通过哈希函数来计算数据存储位置的数据结构
    由一个直接寻址表和一个哈希函数组成
    支持如下操作：
        inser(key,value)：插入
        get(key):存在键为key的值则返回其value
        delete(key):删除键为key的键值对
'''
class LinkList:
    class Node:
        def __init__(self,item=None):
            self.item=item
            self.next=None
    class LinkListIterator:
        def __init__(self,node):
            self.node=node
        def __next__(self):
            cur_node=self.node
            self.node=cur_node.next
            return cur_node.item