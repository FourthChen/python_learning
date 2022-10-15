# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 11:19
# @Author  : sihao
# @File    : 4-线程接受任务.py
import time
import threading

def task(n):
    print("执行任务",n)
    time.sleep(10)
    print('...........')
    print('任务%s执行完毕：'%n)

while True:
    name=input("请输入任务：")
    t=threading.Thread(target=task,args=(name,))
    t.start()