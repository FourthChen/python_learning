
data_list=[]
for i in range(0,300):
    data_list.append('alex_%s'%i)
while True:
    #1.要查看的页面
    page=int(input("请输入你想查看的页数："))

    #2.每页显示10条
    per_page_num=10
    page_data_list=data_list[10*(page-1):10*(page-1)+10]
    for item in page_data_list:
        print(item)