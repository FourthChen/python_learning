# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 23:00
# @Author  : sihao
# @File    : selenium模块.py
from selenium import webdriver
from time import sleep
#后面是浏览器的驱动位置，记得前面加‘r’,'r'是防止转义字符
driver=webdriver.Chrome()