# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 12:38
# @Author  : sihao
# @File    : mysql.py

import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='138304',db='mydb',
                     port=3306,charset='utf8')

cursor=conn.cursor()
cursor.execute("insert into students(name,sex,grade) values(%s,%s,%s)",('张三','女',87))
conn.commit()