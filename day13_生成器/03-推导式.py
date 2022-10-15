
# lst=[]
# for i in range(1,13):
#     lst.append('python'+str(i))
# print(lst)

#推导式：用一句话来生成一个列表
# lst=["python"+str(i) for i in range(1,16) if i%2==1]
# print(lst)

#语法：  [结果  for循环  判断]

#100以内能被3整除的数的平方
# lst=[i*i for i in range(100) if i%3==0]
# print(lst)

#[11,22,33,44] => {0:11,1:22,2:3}
# lst=[11,22,33,44]
# dic={i:lst[i] for i in range(len(lst))if i<2}   #字典推导式就一行
# print(dic)
# #语法 ：{k:v  for循环  条件筛选}

# dic={'jj':'林俊杰','jay':'周杰伦'}
# d={v: k for k,v in dic.items()}#tem()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回。
# print(d)

#集合推导式
# s={i for i in range(100)}#可去重复
# print(s)

lst=[1,3,2,1,5,3,6,5,3,4]
s={el for el in lst}
print(s)