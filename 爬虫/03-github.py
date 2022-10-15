# -*- coding: utf-8 -*-
# @Time    : 2020/5/28 18:11
# @Author  : sihao
# @File    : 03-github.py

import requests
import re
#请求获取token，以便通过post校验
# session=requests.session()
res=requests.get("https://github.com/login")
token=re.findall('name="authenticity_token" value="(.*?)"',res.text)[0]
print(token)
data={
    "login":"5153558140@qq.com",
    "password":"19970429qqq",
    "commit": "Sign in",
    "authenticity_token": token,
    "ga_id": "1686084406.1566739637"
}
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
res=requests.post("https://github.com/session",data=data,headers=headers,cookies=res.cookies.get_dict())

print(res.text)