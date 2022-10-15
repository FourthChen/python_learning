# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 12:47
# @Author  : sihao
# @File    : 11-爬起豆瓣音乐存入MongoDB中.py
import pymongo
import requests
import re
from lxml import etree
import time
client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
musictop=mydb['musictop']

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

def get_url_music(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    music_hrefs=selector.xpath('//a[@class="nbg"]/@href')
    for music_url in music_hrefs:
        get_music_info(music_url)
def get_music_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    name=selector.xpath('//*[@id="wrapper"]/h1/span/text()')[0]
    #author=selector.xpath('//*[@id="info"]/span[1]/span/a/text()')[0]
    author=re.findall('表演者:.*?>(.*?)</a>',html.text,re.S)[0]
    style=re.findall('流派:</span>&nbsp;(.*?)<br />',html.text,re.S)[0].strip()
    time=re.findall('发行时间:</span>&nbsp;(.*?)<br />',html.text,re.S)[0].strip()
    publisher= re.findall('出版者:</span>&nbsp;(.*?)<br />', html.text, re.S)[0].strip()
    score=selector.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]
    print(name,author,style,time,publisher,score)
    info={
        'name':name,
        'author':author,
        'style':style,
        'time':time,
        'publisher':publisher,
        'score':score
    }
    musictop.insert_one(info)
if __name__=='__main__':
    urls=['https://music.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_url_music(url)
        print('---------')
        time.sleep(1)
