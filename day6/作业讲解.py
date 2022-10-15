'''

1：页面显示 序号 + 商品名称 + 商品价格，如：
      		1 电脑 1999
	   		2 鼠标 10
     		…
2：用户输入选择的商品序号，然后打印商品名称及商品价格
3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
4：用户输入Q或者q，退出程序。

'''
goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}, ]

while 1:
    for i in goods:
        # good = i
        print(goods.index(i) + 1,i['name'],i['price'])  #index为下标

    str_input = input('请输入您要选着的商品序号,输入Q/q退出:')

    if str_input.isdigit() and 0 < int(str_input) < len(goods):
        i_index = int(str_input)-1
        print(goods[i_index]['name'],goods[i_index]['price'])
    elif str_input.upper() == 'Q':
        break
    else:
        print('输入有误,请重新输入!') 