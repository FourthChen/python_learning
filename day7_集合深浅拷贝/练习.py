# a='alex'  #这是第一次产生alex
# b='alex'  #这句话不会产生新的字符串
# print(id(a),id(b))

# lst=['jj','jay','谦虚']
# lst1=['jj','jay','谦虚']
#
# print(id(lst),id(lst1)

# a=[1,2,3]
# b=[1,2,3]
# c=b
#
# print(c==a)  #True   #判断的是值
# print(c is a)  #False   #判断两个变量指向的是否同一个对象

# s="alex中"
# bs=s.encode("utf-8")
# print(bs)

#ascii中的内容编码之后还是原来的内容
#中文编码后是\x
bs=b'alex\xe4\xb8\xad'  #用什么编码就用什么解码
print(bs.decode("utf-8"))