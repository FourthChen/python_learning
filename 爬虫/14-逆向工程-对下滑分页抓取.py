# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 18:07
# @Author  : sihao
# @File    : 14-逆向工程-对下滑分页抓取.py
import requests
from bs4 import BeautifulSoup
from lxml import etree
headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

}

urls=['https://www.pexels.com/zh-tw/search/book/?page={}'.format(i) for i in range(1,12)]
list=[]

for url in urls:
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')

    imgs=soup.select('article > a > img')
    print(imgs)
    for img in imgs:
        photo=img.get('src')
        list.append(photo)
print(list)
path = 'E://python学习/爬虫/05-爬取的图片/'
print('---')
for item in list:
    data=requests.get(item,headers=headers)
    fp=open(path+item.split('?')[0][-10:],'wb')
    fp.write(data.content)
    fp.close()