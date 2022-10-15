# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 19:27
# @Author  : sihao
# @File    : 生成决策树.py
import pydotplus
import os
os.environ["PATH"]+=os.pathsep+"C:\Program Files\release\bin"

with open('iris','r',encoding="utf-8") as f:
    dot_data=f.read()

graph=pydotplus.graph_from_dot_data(dot_data)

graph.write_png("决策树iris.png")