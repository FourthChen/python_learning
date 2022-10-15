# # -*- coding: utf-8 -*-
# # @Time    : 2020/5/27 23:11
# # @Author  : sihao
# # @File    : 02-豆瓣.py

import re
import requests
import json
import time
#1.发送请求，获取响应
def get_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    res=requests.get(url,headers=headers)
    return res
#2.解析数据
def parser(res):
    #若用findall 要加r
    # reg=re.findall('<div class="item">.*?<a href="(.*?)">.*?<span class="title">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="rating_num".*?>(.*?)</span>.*?<span class="inq">(.*?)</span>',res.text,re.S)
    # print(reg)
    #(.*?)中的   ?P<url>  其中的url是方便迭代器取值的名字
    reg = re.compile('<div class="item">.*?<a href="(?P<url>.*?)">.*?<span class="title">(?P<title>.*?)</span>.*?<span>(?P<rating_num>.*?)</span>.*?<span class="rating_num".*?>(?P<comment_num>.*?)</span>.*?<span class="inq">(?P<comment>.*?)</span>',
                     re.S)
    #做成迭代器
    ret_iter=reg.finditer(res.text,)
    print("ret_iter",ret_iter)
    # for i in ret_iter:
    #     print(i.group("url"))
    #     print(i.group("title"))
    #     print(i.group("rating_num"))
    #     print(i.group("comment_num"))
    #     print(i.group("comment"))
    return ret_iter
#3.存储数据
def store(ret_iter):
    #储存文件
    movie_info={}
    for i in ret_iter:
        print(i.group("url"))
        print(i.group("title"))
        print(i.group("rating_num"))
        print(i.group("comment_num"))
        print(i.group("comment"))

        movie_info["url"] =i.group("url")
        movie_info["title"] =i.group("title")
        movie_info["rating_num"]=i.group("rating_num")
        movie_info["comment_num"] = i.group("comment_num")
        movie_info["comment"] = i.group("comment")

        with open("douban.txt",'a',encoding='utf-8') as f:
            f.write(json.dumps(movie_info,ensure_ascii=False)+"\n")
def spider(url):
    res=get_page(url)
    ret_iter=parser(res)
    store(ret_iter)


def main():
    count=0
    start=time.time()
    for i in range(25):

        url='https://movie.douban.com/top250?start=%s&filter='%i
        count+=25
        spider(url)
    print("cost time :%s"%(time.time()-start))
if __name__=='__main__':
    main()