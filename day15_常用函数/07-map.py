
lst=[1,4,7,2,5,8]
#求列表中每个数的平方
# ll=[]
# for el in lst:
#     ll.append(el**2)

# def func(el):
#     return el**2
# m=map(func,lst)
# print("__dir__"in dir(m))#把后面的可迭代对象中的每一个元素传递给function，
#
# print(list(m))

#分而治之
# map(func1,map(func2,map(fun3,func4)))

# lst1=[1,2,3,4,5,6]
# lst2=[2,3,4,5,6,7]
# m=map(lambda x,y:x+y,lst1,lst2)
# print(list(m))