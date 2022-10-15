# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 17:01
# @Author  : sihao
# @File    : 21-链表.py
'''
链表是由一系列节点组成的元素集合。每一个节点包含两部分
数据域item和指向下一个节点的指针next
通过节点之间的相互连接，最终串联成一个链表。
'''
'''
节点对象
'''
class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
'''
链条对象
'''
class singlyLinkList:
    '''链条对象'''
    def __init__(self):
        self._head=None
    '''
    链表对象从头部开始，链接一个个节点，
    下面我们添加一个在头部和尾部增加节点的方法。
    '''
    def add(self,item):
        '''
        头部添加节点
        :param item:节点值
        :return:
        '''
        node=Node(item)
        node.next=self._head
        self._head=node
    def append(self,item):
        '''
        尾部添加节点
        :param item:
        :return:
        '''
        cur=self._head
        if not cur: #判断是否为空链表
            self.add(item)
        else:
            node=Node(item)
            while cur.next:
                cur=cur.next
            cur.next=node
    @property
    def is_empty(self):
        """
        判断链表是否为空，只需要看头部是否有节点
        :return:
        """
        if self._head:
            return False
        else:
            return True
    @property
    def length(self):
        """
        获取链表长度
        :return:
        """
        cur=self._head
        n=0
        if not cur :
            return n
        else:
            while cur.next:
                cur=cur.next
                n+=1
            return n+1
    def ergodic(self):
        """
        遍历链表
        :return:
        """
        cur = self._head
        if not cur:
            print("None")
        else:
            while cur.next:
                print(cur.item)
                cur = cur.next
            print(cur.item)

    def insert(self, index, item):
        """
        在指定位置插入节点(设置索引从0开始)
        :param item:
        :return:
        """
        if index==0:#索引为0则头部插入
            self.add(item)
        elif index>=self.length:#索引超过范围则尾部插入
            self.append(item)
        else:
            cur=self._head
            n=1
            while cur.next:
                if n==index:
                    break
                cur=cur.next
                n+=1
            node=Node(item)
            node.next=cur.next
            cur.next=node
    def deltel(self,item):
        """
        删除节点
        :param item:
        :return:
        """
        if self.is_empty:#节点为空的情况
            raise  ValueError('null')
        cur=self._head
        pre=None  #记录删除节点的上一个节点
        if cur.item==item:#删除节点为第一个的情况
            self._head=cur.next
        while cur.next:
            pre=cur
            cur=cur.next
            if cur.item==item:
                pre.next=cur.next

    def search(self, item):
        """
        查找节点是否存在
        :param item:
        :return:
        """
        cur = self._head
        while cur != None :
            if cur.item == item:
                return True
            cur = cur.next
        return False