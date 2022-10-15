# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 20:01
# @Author  : sihao
# @File    : 01.py
from flask import Flask

app=Flask(__name__)

#装饰器添加路由
@app.route("/") #ret_inner=route(index)
def index():
    return "hello world@"

app.add_url_rule("/",view_func=index)  #功能和装饰器一样

app.run(   )