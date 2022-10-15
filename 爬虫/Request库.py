# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 10:05
# @Author  : sihao
# @File    : Request库.py
# import requests
# response=requests.get('http://www.baidu.com/')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)

#各种请求方式
# import requests
# requests.post('http://www.python.org/')
# requests.put('http://www.python.org/')
# requests.delete('http://www.python.org/')
# requests.head('http://www.python.org/')
# requests.options('http://www.python.org/')

#请求
#基本GET请求

import requests
response=requests.get('http://www.python.org/')
print(response.text)
#
#带参数的get请求
# import requests
# data={
#     'name':'gerney',
#     'age':22
# }
# response=requests.get('http://httpbin.org/get',params=data)
# print(response.text)

#解析json
# import requests
# import json
# response=requests.get('http://httpbin.org/get')
# print(type(response.text))
# print(response.json())
# print(json.loads(response.text))
# print(type(response.json()))

#获取二进制数据
# import requests
# response=requests.get('http://github.com/favicon.ico')
# print(type(response.text),type(response.content))
# print(response.text)
# print(response.content)
# #写入（下载图片）
# with open('favicon.ico','wb') as f:
#     f.write(response.content)
#     f.close()


#添加headers
#访问知乎，不加headers时，会出现错误
import requests
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
response=requests.get('http://www.zhihu.com/explore',headers=headers)
print(response.text)

#基本POST请求
# import requests
# data={
#     'name':'gerney',
#     'age':22
# }
# response=requests.post('http://httpbin.org/post',data=data)
# print(response.text)

# import requests
# data={
#     'name':'gerney',
#     'age':22
# }
# headers={
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
# }
# response=requests.post('http://httpbin.org/post',data=data,headers=headers)
# print(response.json())

#响应
#reponse属性
# import requests
# respnse=requests.get('http://www.jianshu.com')
# print(type(respnse.status_code),respnse.status_code)
# print(type(respnse.headers),respnse.headers)
# print(type(respnse.cookies),respnse.cookies)
# print(type(respnse.url),respnse.url)
# print(type(respnse.history),respnse.history)

# #状态码判断
# import requests
# respnse=requests.get('http://www.jianshu.com')
# exit() if not respnse.status_code==200 else print('Request Successfully')

#高级操作

#文件上传
# import requests
# file={'file':open('favicon.ico','rb')}
# respnse=requests.post('http://httpbin.org/post',files=file)
# print(respnse.text)

#获取cookie
# import requests
# response=requests.get('https://www.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+'='+value)


#会话维持
#模拟登录
# import requests
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# response=requests.get('http://httpbin.org/cookies')
# print(response.text)
#
# import requests
# s=requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response=s.get('http://httpbin.org/cookies')
# print(response.text)

#证书验证
# import requests
# response=requests.get('http://www.12306.cn')
# print(response.status_code)
#
# import requests
# response=requests.get('http://www.12306.cn',verify=False)
# print(response.status_code)
#
# import requests
# response=requests.get('http://www.12306.cn')
# print(response.status_code)

#代理
# import requests
# proxies={
#     'http':'http://127.0.0.1:9743',
#     'https':'https://127.0.0.1:9743',
# }
#
# response=requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)

#超时设置
# import requests
# from requests.exceptions import ReadTimeout
# try:
#     response=requests.get('http://httpbin.org/get',timeout=0.5)
#     print(response.status_codes)
# except ReadTimeout:
#     print('Timeout')

#认证设置
# import requests
# from requests.auth import HTTPBasicAuth
#
# r=requests.get('http://120.27.34.34:9001')
# print(r.status_code)

#异常处理
import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException
try:
    response=requests.get('http://httpbin.org/get',timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Time out')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')