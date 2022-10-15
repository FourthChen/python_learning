
# lst=['白蛇传','骷髅叹','庄周闲游']
# # it=lst.__iter__()
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
#
# it=iter(lst)  #内部封装的就是__iter__()
# print(it.__next__())
# print(next(it))  #内部封装的就是__next__()

# lst=(1,2,3)
# print(id(lst))
# print(hash(lst))#目的是为了存储，计算之后是一个数字，hash值尽量的不要重复
#
# dic={'jay':'周杰伦','jj':'林俊杰'}

# a=1.25
# print(type(a))
# print(bin(5))#5的二进制 0b二进制
# print(oct(8)) #0o八进制
# print(hex(16)) #0x十六进制

# print(abs(-8))  #绝对值
# print(divmod(10,2))  #计算商和余数
# print(round(3.3)) #四舍五入
# print(pow(2,3))#2的3次幂
# print(pow(2,3,2))#2的3次幂mod2

# print(sum([1,2,3,4,5],3))
# print(min(1,2,3))
# print(max(2,1,4,2))

# lst=['马化腾','马云']
# ll=reversed(lst)
# print(list(ll))#reversed()翻转，返回列表

#zip
# lst1={'甜蜜蜜','往事只能回味'}
# lst2={'邓丽君','韩宝仪'}
# lst3={'2000','3000'}
# a=zip(lst1,lst2,lst3) #水桶效应
# print("__iter__"in dir(a))  #可迭代的
# for el in a:
#     print(el)

# s="5+6"
# ret=eval(s) #动态执行一个代码片段，侧重点在返回上
# print(ret)
# a="{'name':'汪峰','age':'48'}" #json,  像字典一样的东西
# d=eval(a)  #还原回字典，列表
# print(d['name'])

s="a=10"
exec(s) #执行代码
print(a)  #pycharm里的报错信息，不一定是对的