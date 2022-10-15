#
# lst=['张无忌','张铁林','赵宜宁','马大叔']
# def func(el):
#     if el[0]=='张':
#         return False  #不想要的
#     else:
#         return True  #想要的
# #筛选
# f=filter(func,lst)  #将lst中的每一项传递给func，所有返回Ture的都会保留，所有返回False的都会剔除
# print("__iter__"in dir(f))#判断是否可以进行迭代
# for el in f:
#     print(el)

lst=[
    {'name':'汪峰','score':48},
    {'name':'章子怡','score':39},
    {'name':'赵宜宁','score':97}
]
f=filter(lambda el:el['score']<60,lst)
print(list(f))