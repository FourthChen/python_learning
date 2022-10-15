# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 14:06
# @Author  : sihao
# @File    : 25-二叉搜索树.py
'''
设x是二叉树的一个节点，
y是x左子树的一个节点,那么y.key<=x.key
y是x右子树的一个节点,那么y.key>=x.key

二叉搜索树的操作：查询，插入，删除
'''
class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None  #左孩子
        self.rchild=None  #右孩子
        self.parent=None

class BST:
    def __init__(self,li=None):
        self.root=None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self,node,val):
        if not node:
            node=BiTreeNode(val)
        elif val<node.data:
            node.lchild=node.insert(node.lchild,val)
            node.lchild.parent=node
        elif val>node:
            node.rchild=node.insert(node.rchild,val)
            node.rchild.parent=node
        return node
    #不用递归
    def insert_no_rec(self,val):
        p=self.root
        if not p: #空树
            self.root=BiTreeNode(val)
            return
        while True:
            if val<p.data:
                if p.lchild:
                    p=p.lchild
                else:
                    p.lchild=BiTreeNode(val)
                    p.lchild.parent=p
            elif val>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=BiTreeNode(val)
                    p.rchild.parent=p
            else:
                return
    #查询
    def query(self,node,val):
        if not node:
           return None
        if node.data<val:
            return self.query(node.rchild,val)
        elif node.data>val:
            return self.query(node.lchild, val)
        else:
            return node
    #不用递归的查询
    def query_no_rec(self,val):
        p=self.root
        while p:
            if p.data<val:
                p=p.rchild
            elif p.data>val:
                p=p.lchild
            else:
                return p
        return None
    #前序遍历
    def pre_order(self,root):
        if root:
            print(root.data, end='')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)


    # 中序遍历
    def in_order(self,root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end='')
            self.in_order(root.rchild)


    # 后序遍历
    def post_order(self,root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end='')
    def __remove_node_1(self,node):
        #node是叶子节点
        if not node.parent:  #根节点
            self.root=None
        if node==node.parent.lchild: #node是父亲的左孩子
            node.parent.lchild=None
        else:
            node.parent.rchild=None
    def __remove_node_21(self,node):
        #只有一个左孩子
        if not node.parent:
            self.root=node.lchild
            node.lchild.parent=None
        elif node==node.parent.lchild:
            node.parent.lchild=node.lchild
            node.lchild.parent=node.parent
        else:
            node.parent.rchild=node.rchild
            node.rchild.parent=node.parent
    def __remove_node_22(self,node):
        #只有一个右孩子
        if not node.parent:
            self.root=node.rchild
        elif node==node.parent.lchild:
            node.parent.lchild=node.rchild
            node.rchild.parent=node.parent
        else:
            node.parent.rchild=node.rchild
            node.rchild.parent=node.parent

    #删除
    def delete(self,val):
        if self.root:
            node=self.query_no_rec(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            elif not node.rchild:  #只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:
                self.__remove_node_22(node)
            else:  #两个孩子都有
                min_node=node.rchild
                while min_node.lchild:
                    min_node=min_node.lchild
                node.data=min_node.data
                #删除min_node
                if min_node.rchild:
                    self.__remove_node_22(node)
                else:
                    self.__remove_node_1(node)
tree=BST([4,6,7,9,2,1,3,5,8])
tree.in_order(tree.root)
print("")

tree.delete(3)
tree.in_order(tree.root)
