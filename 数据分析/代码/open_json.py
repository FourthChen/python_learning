'''
JSON数据是数据传输最常用的格式之一
'''
import json

json_data=open('E:/python学习/数据分析/数据/data-text.json').read()

data=json.loads(json_data)

for item in data:
    print(item)