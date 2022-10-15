# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 17:37
# @Author  : sihao
# @File    : page_spider.py
import requests
from lxml import etree
import pymongo
import time
client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
tongcheng_url=mydb['tongcheng_url']
tongcheng_info=mydb['tongcheng_info']
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

def get_links(channel,pages):
