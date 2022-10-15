
from csv import DictReader
'''
[func(x) for x in iter_x],  iter_x是一个可迭代对象，将iter_x的每一行或每一个值传入func(x)

'''
data_rdr=DictReader(open('E:/python学习/数据分析/数据/mn.csv','r',encoding="utf-8"))
header_rdr=DictReader(open('E:/python学习/数据分析/数据/mn_headers.csv','r',encoding="utf-8"))

data_rows=[d for d in data_rdr]
header_rows=[h for h in header_rdr]

print(data_rows[:5])
print(header_rows[:5])