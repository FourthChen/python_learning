
'''
1.让用户输入金额
2，选择要购买的商品加入购物车
3.当商品的总价超过了你的金额提示余额不足
4.让用户输入N结算，输入Q退出
5.用户退出时提示还剩多钱
'''
goods=[
    {'name':"电脑",'price':1999},
    {'name':"鼠标",'price':10},
    {'name':"美女",'price':50},
    {'name':"游艇",'price':20},
    {'name':"火箭",'price':250}
]
shop_car={}   #健==列表的索引     值==商品的数量
fei_yong=0
money=input('请输入您的金额：')
if money.isdigit():  #判断money是数字
    while 1:
        for i in range(len(goods)):
            print(i+1,goods[i]['name'],goods[i]['price'])
            #=========商品展示=============
        choose=input('请输入您需要的商品序号:')
    #===========================让商品增加到购物车
        # 让用户输入商品序号并判断是不是数字以及在不在正常范围内
        if choose.isdigit() and 0<int(choose)<=len(goods):
              #通过用户输入的内容减一就获取到商品的索引
            int_index=int(choose)-1
            if shop_car.get(int_index) == None:
                # shop_car[0]=1
                shop_car[int_index] =1
            else:
                shop_car[int_index]=shop_car[int_index]+1
    #========================'...==pass'=======================================
        elif choose.upper() == 'N':
            #结算
            for f in shop_car:
                fei_yong=fei_yong+ shop_car[f] *goods[f]['price']
            if int(money)- fei_yong >=0:
                for k in shop_car:
                    print('您购买的商品是{},单价{},数量{}'.format(goods[k]["name"],goods[k]["price"],shop_car[k]))
            else:
                print('余额不足了')
                # for i,v in enumerate(shop_car,1):
                #     print('{}{}{}'.format(i,goods[v]['name'],shop_car[v]))
                # str_del =int(input('请删除商品对应的序号'))
                # shop_car[str_del-1]=shop_car[str_del-1]-1
        elif choose.upper() =='Q':
            #退出
            print('您此次共消费{},剩余{}'.format(fei_yong,int(money)-fei_yong))
            break
        else:
            print('输入有误，请重新输入')
else:
    print('请正确输入')