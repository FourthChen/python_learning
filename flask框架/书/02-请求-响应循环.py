# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 15:42
# @Author  : sihao
# @File    : 02-请求-响应循环.py
from flask import Flask
'''
Flask 从客户端收到请求时，要让视图函数能访问一些对象，这样才能处理请求。
请求对象就是一个很好的例子，它封装了客户端发送的 HTTP 请求。
'''
'''
线程是可单独管理的最小指令集。进程经常使用多个活动线程，有时还会共享内存或文件句柄等资源。 
多线程 Web 服务器会创建一个线程池，再从线程池中选择一个线程用于处理接收到的请求。

在 Flask 中有两种上下文： 程序上下文和请求上下文。
'''
app=Flask(__name__)
app.route('/')
def index():
    # request为请求上下文，请求对象，封装了客户端发出的HTTP请求中的内容
    user_agent=request.headers.get('User-Agent')
    return '<p>your browser is %s</p>'%user_agent

#URL 映射是 URL 和视图函数之间的对应关系
#Flask 使用 app.route 修饰器或者非修饰器形式的 app.add_url_rule() 生成映射。

'''
请求钩子有时在处理请求之前或之后执行代码会很有用。
请求钩子使用修饰器实现。 Flask 支持以下 4 种钩子:
    • before_first_request：注册一个函数，在处理第一个请求之前运行。
    • before_request：注册一个函数，在每次请求之前运行。
    • after_request：注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
    • teardown_request：注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。

在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量 g。
'''

#下述视图函数返回一个 400 状态码，表示请求无效
@app.route('/')
def index():
    return '<h1>Bad Request</h1>',400


#下例创建了一个响应对象，然后设置了 cookie：
from  flask import make_response
@app.route('/')
def index():
    response=make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer','42')
    return response

'''
重定向经常在 Web 表单中使用，
重定向经常使用 302 状态码表示，
指向的地址由 Location 首部提供。
重定向响应可以使用3个值形式的返回值生成， 也可在 Response 对象中设定。
不过，由于使用频繁，Flask 提供了redirect()辅助函数，用于生成这种响应：
'''
from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')

'''
还有一种特殊的响应由 abort 函数生成，用于处理错误。
在下面这个例子中，如果 URL 中动态参数 id 对应的用户不存在，就返回状态码 404：
'''
from flask import abort
@app.route('/user/<id>')
def get_user(id):
    user=load_user(id)
    if not user:
        abort(404)
    return '<h1>hello,%s</h1>'%user.name