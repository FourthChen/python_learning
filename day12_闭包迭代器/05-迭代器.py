
# s=123
# for i in s:
#     print(i)
# print(dir(str))  #通过dir查看xx类型的数据可以执行哪些方法,__iter__
# print(dir(list))  #__iter__
# print(dir(int))  #没有 __iter__
#所有的带__iter__可疑使用for循环的，可迭代对象
#可迭代对象可以使用__iter__()来获取到迭代器
#迭代器里面有__next()__
# s='xx喜欢xx'
# it=s.__iter__()  #获取迭代器
# print(it.__next__())  # x
# print(it.__next__())  # x
# print(it.__next__())  # 喜
# print(it.__next__())  # 欢
# print(it.__next__())  # x
# print(it.__next__())  # x

#迭代器模拟for循环---------------牢记
# lst=['赵宜宁','史可新','姚明']
# # for el in lst:  #底层用的就是迭代器
# #     print(el)
# it=lst.__iter__()
# while 1:
#     try:           #尝试执行
#         el=it.__next__()
#         print(el)
#     except StopIteration:  #处理错误
#         break
#
#
# from collections import Iterable   #可迭代对象
# from collections import Iterator   #迭代器
# print(isinstance(lst,Iterable))   #判断lst是不是可迭代对象
# print(isinstance(lst,Iterator))   #判断lst是不是迭代器

lst=['赵四','花生哥']
it=lst.__iter__()
#list(参数)会把参数循环迭代
s=list(it)  #在list中一定存在for，一定__next()__
print(s)