'''
CSV是指将数据列用逗号分隔的文件
'''

import csv

#以列表的形式打开
# csvfile=open('E:/python学习/数据分析/数据/data-text.csv','r',encoding='utf-8')
# reader=csv.reader(csvfile)
#
# for row in reader:
#     print(row)

#以字典的形式打开
csvfile=open('E:/python学习/数据分析/数据/data-text.csv','r',encoding='utf-8')
reader=csv.DictReader(csvfile)

for row in reader:
    print(row)