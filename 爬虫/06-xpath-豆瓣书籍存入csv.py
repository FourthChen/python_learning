# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 17:05
# @Author  : sihao
# @File    : 06-xpath-豆瓣书籍存入csv.py
from lxml import etree
import requests
import csv

fp=open('doubanbook.csv','wt',newline='',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))

urls=['https://book.douban.com/top250?start={}'.format(str(i)) for  i in range(0,250,25)]

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

for url in urls:
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text) #Lxml解析数据
    infos=selector.xpath('//*[@class="item"]')
    for info in infos:
        name=info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_infos = info.xpath('td/p/text()')[0]
        author=book_infos.split('/')[0]
        publisher=book_infos.split('/')[-3]
        date=book_infos.split('/')[-2]
        price=book_infos.split('/')[-1]
        comments=info.xpath('td/p/span/text()')
        writer.writerow((name,url,author,publisher,date,price,comments))
fp.close()