# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 15:18
# @Author  : sihao
# @File    : 01-初始化.py
from flask import Flask
#Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。
# app=Flask(__name__)
'''
修饰器是 Python 语言的标准特性，可以使用不同的方式修改函数的行为。惯
常用法是使用修饰器把函数注册为事件的处理程序。
'''
#用程序实例提供的 app.route 修饰器，把修饰的函数注册为路由。
# index() 函数注册为程序根地址的处理程序。
'''
像 index() 这样的函数称为视图函数。视图函数返回的响应可以是包含
HTML 的简单字符串，也可以是复杂的表单，
'''
# @app.route('/')
# def index():
#     return '<h1>hello,world!</h1>'
# #用 run 方法启动 Flask 集成的开发 Web 服务器
# if __name__== '__main__' :
#     app.run(debug=True)

'''
下列是包含动态路由得Flask程序
'''
from flask import Flask
app=Flask(__name__)
@app.route('/')
def index():
    return '<h1>hello,world!</h1>'
'''
下面修饰器尖括号中的内容就是动态部分，任何能匹配静态部分的 URL 都会映射到这个路由上。
调用视图函数时， Flask 会将动态部分作为参数传入函数。
在这个视图函数中，参数用于生成针对个人的欢迎消息
'''

@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s!</h1>' %name

if __name__=='__main__':
    app.run(debug=True)
