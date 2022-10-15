# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 19:21
# @Author  : sihao
# @File    : hello.py
# from flask import Flask,render_template
#
# #...
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/user/<name>')
# def user():
#     return render_template('user.html',name=name)


#初始化Flask-Bootstrap
from flask_bootstrap import Bootstrap
#...
bootstrap=Bootstrap(app)