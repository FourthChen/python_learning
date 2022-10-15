# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 21:13
# @Author  : sihao
# @File    : 01汽车之家新闻.py
import requests
from bs4 import BeautifulSoup
#练习一：获取一个标题
# response=requests.get('https://www.autohome.com.cn/news/')
# response.encoding='gbk'
# # print(response.text)
# soup=BeautifulSoup(response.text,'html.parser')
# tag=soup.find(id='auto-channel-lazyload-article')
# h3=tag.find(name='h3')
# print(h3)


#找到所有新闻
#标题，简介，url，图片
response=requests.get('https://www.autohome.com.cn/news/')
response.encoding='gbk'
soup=BeautifulSoup(response.text,'html.parser')
li_list=soup.find(id='auto-channel-lazyload-article').find_all(name='li')
print(li_list)
# for li in li_list:
#     title=li.find('h3')
#     if not title:
#         continue
#     summary=li.find('p').text
#     url=li.find('a').get('href')
#     img = li.find('img').get('src')
#     print(title.text,url, summary,img)
#     print('================')


