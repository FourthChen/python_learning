# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 12:40
# @Author  : sihao
# @File    : 23-树的实例-模拟文件系统.py

class Node:
    def __init__(self,name,type='dir'):
        self.name=name
        self.type=type #"dir" or "file"
        self.children=[]
        self.partent=None
    def __repr__(self):
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root=Node("/")
        self.now=self.root
    def mkdir(self,name):
        #name是以 / 结尾
        if name[-1] !="/":
            name+="/"
        node=Node(name)
        self.now.children.append(node)
        node.parent=self.now
    def ls(self):
        return self.now.children

    def cd(self,name):
        """
        支持相对路径
        :param name:
        :return:
        """
        if name[-1] !="/":
            name+="/"
        if name=='../':
            self.now=self.now.parent
        for child in self.now.children:
            if child.name==name:
                self.now=child
        return ValueError('invaild dir')

tree=FileSystemTree()

tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')

tree.cd("bin/")
tree.mkdir('python/')
tree.cd("../")
print(tree.ls())
