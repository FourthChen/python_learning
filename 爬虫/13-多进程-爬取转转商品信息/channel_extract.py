# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 17:07
# @Author  : sihao
# @File    : channel_extract.py
import requests
from lxml import etree

start_url='https://cs.58.com/sale.shtml'
url_host='https://cs.58.com'
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
def get_channel_urls(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//div[@class="lbsear"]/div/ul/li')

    for info in infos:
        class_urls=info.xpath('ul/li/b/a/@href')
        print(class_urls)
        for class_url in class_urls:
            print(url_host+class_url)


get_channel_urls(start_url)