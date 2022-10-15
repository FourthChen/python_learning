
from wsgiref.simple_server import make_server

'''
1.路由的分发器，负责把url匹配到对应的函数
2.开发好对应的业务函数
3.一个请求来了之后，先走路由分发器，如果找到对应的function，就执行，如果没有找到就返回404
'''
def book(environ,start_response):
    print("book page")
    start_response("200 OK", [("Content-Type", 'text/html;charset=utf-8')])
    return [bytes('<h2>123qazwsx</h2>', encoding="utf-8")]

def cloth(environ,start_response):
    print("cloth path")
    return

def url_dispacher(environ,start_response):
    urls={
        "/book":book,
        "/cloth":cloth,
    }
    return urls

def run_server(environ,start_response):
    print("dsdsdsdd",environ)

    urls=url_dispacher()  #拿到所有的url
    request_url=environ.get("PATH_INFO")
    print("request url",request_url)

    if request_url in urls:
        func=urls[request_url](environ,start_response)
        return func
    else:
        start_response("200 OK", [("Content-Type", 'text/html;charset=utf-8')])
        return [bytes('404',encoding='utf-8')]
    # start_response("200 OK",[("Content-Type",'text/html;charset=utf-8')])
    # return [bytes('<h2>qazwsx</h2>',encoding="utf-8")]
s=make_server('localhost',8009,run_server)
s.serve_forever()

# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

# from wsgiref.simple_server import make_server
#
#
# def western():
#     return "欢迎来到欧美专区"
#
# def japan():
#     return "欢迎来到日本人专区"
#
#
# def routers():
#     """负责把url与对应的方法关联起来"""
#     urlpatterns = (
#         ('/western/',western),
#         ('/japan/',japan),
#     )
#
#     return urlpatterns
#
#
# def run_server(environ, start_response):
#     """
#     当有用户在浏览器上访问：http://127.0.0.1:8000/, 立即执行该函数并将函数的返回值返回给用户浏览器
#     :param environ: 请求相关内容，比如浏览器类型、版本、来源地址、url等
#     :param start_response: 响应相关
#     :return:
#     """
#     start_response('200 OK',[('Content-Type', 'text/html;charset=utf-8')])
#     url = environ.get("PATH_INFO")
#     urlpatterns = routers()
#
#     func = None
#
#     for item in urlpatterns:
#         if item[0] == url:
#             func = item[1]
#             break
#     if func:
#         return [bytes(func(),encoding="utf-8"),]
#     else:
#         return [bytes('404 not found.',encoding="utf-8"),]
#
# if __name__ == '__main__':
#     httpd = make_server('localhost',8001,run_server)
#     httpd.serve_forever()
#
