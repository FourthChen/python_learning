import xlrd
import pprint
'''
用pprint语句对于复杂的数据结构输出时要容易很多
'''
book=xlrd.open_workbook('E:/python学习/数据分析/数据/SOWC 2014 Stat Tables_Table 9.xlsx')
sheet=book.sheet_by_name('Table 9 ')
data={}

for i in range(14,sheet.nrows):
    #从第14行开始，因为这是国家数据的起点
    row=sheet.row_values(i)
    country=row[1]

    data[country]={
        'child_labor':{
            'total':[row[4],row[5]],
            'male':[row[6],row[7]],
            'female':[row[8],row[9]],
        },
        'child_marriage':{
            'married_by_15':[row[10],row[11]],
            'married_by_18':[row[12],row[13]],
        }
    }

    if country =='Zimbabwe':
        break
    pprint.pprint(data)