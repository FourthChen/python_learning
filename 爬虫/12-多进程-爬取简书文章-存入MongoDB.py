# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 14:49
# @Author  : sihao
# @File    : 12-多进程-爬取简书文章-存入MongoDB.py
import requests
from lxml import etree
import pymongo
from multiprocessing import Pool
client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
jianshu_shouye=mydb['jianshu_shouye']
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

def get_jianshu_info(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//ul[@class="note-list"]/li')
    print(infos)
    for info in infos:
        author=info.xpath('div/div/a/text()')[0]
        title=info.xpath('div/a/text()')[0]
        print(author,title)


if __name__=='__main__':
    # urls=['https://www.jianshu.com/c/bDHhpK?order_by=commented_at&page={}'.format(str(i)) for i in range(1,10)]
    urls = ['https://www.jianshu.com/c/bDHhpK']
    pool=Pool(processes=4)
    pool.map(get_jianshu_info,urls)