# == 比较   比较的是值
# a = 'alex'
# b = 'alex'
# print(a==b)     #Ture

#is  是  比较  比较的是内存地址

# a= 'alex'
# print(id(a))  #打印a的地址 ：7559968
#
# n=10
# print(id(n))
#
# li=[1,2,3]
# print(id(li))
#字符串
# a='alex'
# b='alex'
# print(a is b)   #True
# #数字
# n=10
# n1=10
# print(n is n1)   #True
# #========================================
#小数据池
    # 数字数小据池的范围：  -5~256
    # 字符串中如果有特殊字符他们的内存地址就不一样
    # 字符串中单个*20以内他们的内存地址一样
# a='alex@'
# a1='alex@'
# print(a is a1)  #False
#
# n= -5
# n1=-5
# print(n is n1) #False
a='a'*20
b='a'*20
print(a is b)  #True
# #列表
# li=[1,2,3]
# li2=[1,2,3]
# print(li is li2)   #False
# #元组
# tu=(1,2,3)
# tu1=(1,2,3)
# print(tu is tu1)   #False
# #字典
# dic={'name':'alex'}
# dic1={'name':'alex'}
# print(dic is dic1)    #False


#总结  ：
    # == 比较   比较的是两边的值
    # is  比较   比较的是内存地址   用的是id()