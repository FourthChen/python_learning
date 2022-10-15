# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 12:12
# @Author  : sihao
# @File    : 09-xpath-爬取用户地址信息.py
import requests
from lxml import etree
import csv
import json

fp=open('map.csv','wt',newline='',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow=(('address','longitude','latitde'))
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

def get_user_url(url):
    url_part='http://www.qiushibaike.com'
    res=requests.get(url,headers=headers)
    selector=etree.HTML(res.text)
    url_infos=selector.xpath('')
