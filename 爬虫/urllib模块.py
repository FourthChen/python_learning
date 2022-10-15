# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 08:47
# @Author  : sihao
# @File    : urllib模块.py
# import urllib.request
# response=urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# import urllib.parse
# import urllib.request
# data=bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# import urllib.request
# response=urllib.request.urlopen('http://httpbin.org/get',timeout=1)
# print(response.read())

# import socket
# import urllib.request
# import urllib.error
# #设置了超时的时间
# try:
#     response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

#响应
#响应类型
# import urllib.request
# response=urllib.request.urlopen('http://www.python.org')
# print(type(response))
#
# #响应码，响应头
# import urllib.request
# response=urllib.request.urlopen('http://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

#Request
# import urllib.request
# request=urllib.request.Request('http://www.python.org')
# response=urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
#
# from urllib import request,parse
# url='https://www.python.org/'
# headers={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# }

