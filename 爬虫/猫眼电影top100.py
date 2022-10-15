# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 22:08
# @Author  : sihao
# @File    : 猫眼电影top100.py
'''
爬虫框架：
    1.抓取单页内容
    2.正则表达式分析
    3.保存在文件
    4.开启循环及多线程
'''
import requests
import re
from requests.exceptions import RequestException
def get_one_page(url):
    try:
        headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
            }
        response=requests.get(url,headers=headers)
        response.encoding='utf-8'
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a')

def main():
    url='https://maoyan.com/board/4'
    html=get_one_page(url)
    print(html)
if __name__ == '__main__':
    main()


