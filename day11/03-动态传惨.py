
# def chi(good_food,no_good_food,drink,ice_cream):
#     print(good_food,no_good_food,drink,ice_cream)
#
# chi('盖浇饭','腊肠','橙汁','哈根达斯')

#   *表示接收位置参数的动态参数，接受到的是元组
# def chi(*food,location,name):    #参数名是food   *表示动态传参
#     print(name+'在'+location+'要吃',food)
# chi('火锅','盖浇饭','龙虾面',location='北京',name='刘旺')

#关键词的动态传参
def chi(**food):
    print(food)   #结果是字典

chi(good_food='狗不理',no_good_food='汉堡')

#顺序
# 位置参数，*args，默认值参数，**kwargs
# 以上参数可以随意搭配使用

# #1.实参
#     位置参数
#     关键字参数
#     混合参数（位置，关键字）
# #2.形参
#     位置参数
#     默认值参数
#     动态传参：
#        *args：位置参数动态传参
#         **kwargs：关键字参数动态传参
#     顺序：位置，*args，默认值，**kwargs
# def fun(a,*args,c='haha',**kwargs):
#     print(a, args ,c,kwargs)
# fun(1,2,3,d=5,c=6)

#单行注释
'''多行注释'''
#函数注释
# def func(a,b):
# #     '''
# #     解释这个函数的功能，这个函数是用来计算a和b的和
# #     :param a:  #解释第一个数据
# #     :param b:  #解释第二个数据
# #     :return:   返回的是两个数的和
# #     '''
# #     return a + b
# # func(func.__doc__) #document文档

#接受所有的参数
# def func(*args,**kwargs):  #无敌  8args相当于一个聚合的作用
#     print(args,kwargs)
# func(1,2,3,4,b=6,c=7)

# def func(*food):     #聚合，位置参数
#     print(food)
# lst=['鸡蛋','煎饼果子']
# func(*lst)  #打散，把list，tuple，set，str进行迭代打散

#聚合成关键词参数
# def func(**kwargs):
#     print(kwargs)
# dic={'name':'alex','age':'18'}
# func(**dic)   #打散成关键字参数

