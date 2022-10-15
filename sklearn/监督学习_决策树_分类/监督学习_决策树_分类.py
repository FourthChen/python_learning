# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 09:43
# @Author  : sihao
# @File    : 监督学习_决策树_分类.py
from sklearn import tree
import graphviz
from sklearn import datasets

#1.给定数据集

iris=datasets.load_iris()
feature_names=['花萼的长度 (cm)', '花萼的宽度 (cm)', '花瓣的长度 (cm)', '花瓣的宽度 (cm)']
print(iris.feature_names)
print(iris.target_names)
#2.实例化(告诉计算机，用哪种方法)

clf=tree.DecisionTreeClassifier()

#3.训练数据集
clf.fit(iris.data,iris.target)

#4.画出决策树

dot_data=tree.export_graphviz(clf,
                              out_file=None,
                              feature_names=feature_names,
                              class_names=iris.target_names,
                              filled=True,
                              rounded=True,
                              special_characters=True)

grap=graphviz.Source(dot_data)
grap.render('iris')

with open('iris.text','w',encoding="utf-8") as f:
    f.writelines(dot_data)