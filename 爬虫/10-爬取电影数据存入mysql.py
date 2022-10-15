# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 13:20
# @Author  : sihao
# @File    : 10-爬取电影数据存入mysql.py
import pymysql
import requests
import re
import time
from lxml import etree

conn=pymysql.connect(host='localhost',user='root',passwd='138304',db='mydb',
                     port=3306,charset='utf8')
cursor=conn.cursor()
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
def get_moive_url(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    movie_hrefs=selector.xpath('//div[@class="hd"]/a/@href')
    for movie_href in movie_hrefs:
        get_movie_info(movie_href)


def get_movie_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    try:
        name=selector.xpath('//*[@id="content"]/h1/span[1]/text()')[0]

        director=selector.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]
        actors=selector.xpath('//*[@id="info"]/span[3]/span[2]')[0]
        actor=actors.xpath('string(.)')
        style=re.findall('<span property="v:genre">(.*?)</span>',html.text,re.S)
        print(style)
        # country=selector.xpath('//*[@id="info"]/span[8]/text()')
        country=re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>',html.text,re.S)
        print(country)
        cursor.execute(
            "insert into doubanmovie (name,director,actor,style,country) values(%s,%s,%s,%s,%s)",(str(name),str(director),str(actor),str(style),str(country)))
        print('++++++++++++')
    except IndexError:
        pass




if __name__=='__main__':
    urls=['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
    for url in urls:
        get_moive_url(url)
        print('---------')
        time.sleep(1)
        conn.commit()
    print("=============")
