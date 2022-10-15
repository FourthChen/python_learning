# s={'a':1,'b':2,'v':6}
# # sss=0
# # t=0
# # for i in s:
# #     ss=s[i]
# #     sss  =sss + ss
# #     t=t+1
# # print(sss)
# # print(t)

#将列表转换成字符串，每个元素之间用_拼接
# s='_'.join(['123','234','345'])
# print(s)

#把字符串以“_”为分隔符进行切割，并转换成列表
# ss="123_234_345"
# ss.split("_")

#字符串转换成列表：split()
#把列表转换成字符串：join()

# s="_".join("马化腾")
# print(s)
# #join(可迭代对象)

# lst=["紫云","大云","玉溪","紫钻"]
# # lst.clear()  #清空列表
# for el in lst:   #有一个变量来记录当前循环的位置
#     lst.remove(el)
# print(lst)


#关于列表的删除
# lst=["紫云","大云","玉溪","紫钻"]
# new_lst=[]
# for el in lst:
#     new_lst.append(el)
# #循环新列表，删除老列表
# for el in new_lst:
#     lst.remove(el)
# print(lst)

#把姓张的删掉
# lst=['张国荣','张铁林','张国立','王菲']
# new_lst=[]
# for el in lst:
#     if el[0]=="张":
#         new_lst.append(el)
# for el in new_lst:
#     lst.remove(el)
# print(lst)
# print(new_lst)

#字典-------删除字典
dic={'提莫':"冯提莫",'发姐':'陈一发','55开':'卢本伟'}
# dic.clear()
# print(dic)
lst=[]
for el in dic:
    lst.append(el)
for el in lst:
    dic.pop(el)
print(dic)

#综上，列表和字典都不能在循环的时候进行删除
#字典在循环的时候不允许改变大小

