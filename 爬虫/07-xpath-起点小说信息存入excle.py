# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 17:43
# @Author  : sihao
# @File    : 07-xpath-起点小说信息存入excle.py
import xlwt
import requests
from lxml import etree
import time
all_infos=[]
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
def get_info(url):
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//ul[@class="all-img-list cf"]/li')
    print(infos)
    # for info in infos:
    #     title=info.xpath('div[2]/h4/a/text()')[0]
    #     author=info.xpath('div[2]/p[1]/a[1]/text()')[0]
    #     style_1=info.xpath('div[2]/p[1]/a[2]/text()')[0]
    #     style_2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
    #     style=style_1+'.'+style_2
    #     introduce = info.xpath('div[2]/p[2]/text()')[0].strip()
    #     info_list=[title,author,style,introduce]
    #     all_infos.append(info_list)
    # time.sleep(1)

if __name__=='__main__':
    urls=['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page={}'.format(str(i)) for  i in range(1,500)]
    for url in urls:
        get_info(url)
#
#     header=['title','author','style','introduce']  #定义表头
#     book=xlwt.Workbook(encoding='utf-8')
#     sheet=book.add_sheet('Sheet1')
#     for h in range(len(header)):
#         sheet.write(0,h,header[h])
#     i=1
#     for list in all_infos:
#         j=0
#         for data in list:
#             sheet.write(i,j,data)
#             j+=1
#         i+=1
# book.save('xiaoshuo.xls')