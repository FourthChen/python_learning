# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 14:26
# @Author  : sihao
# @File    : xpath解析器.py

from lxml import etree

#本地文件处理方法
tree=etree.parse(文件名)
tree.xpath('xpath表达式')

#本网络数据处理方法
tree=etree.HTML(网页内容字符串)
tree.xpath('xpath表达式')

#表达式的语法
#属性定位
"""
例如: //div,查找网页内的所有div
例如: //div[@class='box'],查找class为box的div
例如: //div[@class='box'][2],查找符合条件的第2个div
例如: //ul/li/div/a/img,查找ul下的li下的div下的a下的img标签
例如://ul/li/div/a/img/@src, 查找ul下的li下的div下的a下的img标签的src属性
例如://a/text(), 获取a标签之间的文本(一级文本)
例如://div[@class='box']//text(), 获取class为div下的所有文本
例如://div[contains(@class,'zhangsan')] 查找class中包含zhangsan的div
例如://*[@name='lisi']查找所有name为lisi的元素
"""