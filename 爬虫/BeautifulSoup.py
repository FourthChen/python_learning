# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 15:17
# @Author  : sihao
# @File    : BeautifulSoup.py
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p id="my p" class="title"><b id="bbb" class="boldest">The Dormouse's story</b>
</p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup=BeautifulSoup(html_doc,'lxml')
# print(soup.p)
# print(soup.find_all('a'))

######tag对象 ##############
# print(soup.a.text)
# print(soup.a.attrs.get('id'))

#######findall()#############

# print(soup.find_all('a'))
# print(soup.find_all('a',{"id":'link1'}))

import re
###########五种过滤器
# print(soup.find_all("a"))
# #按正则
print(soup.find_all(re.compile("b")))
#加列表
print(soup.find_all(['a','b']))

print()