#普通的正常函数
# def func(n):
#     return n*n
# ret=func(9)
# print(ret)
#
# #匿名函数,语法：lambda 参数：返回值
# a=lambda n:n*n
# ret=a(9)
# print(ret)
#
# print(func.__name__)#查看函数的名字
# print(a.__name__) #__name__的值都是<lambda>

# def func():
#     return a+b
#
# x= lambda a,b:a+b
# print(x(1,2))

# def func(x,y):
#     return x,y
# print(func(1,2))
#
# x=lambda x,y:(x,y)  #笔试题
# print(x(1231,23))

#匿名函数，给函数传递参数，返回最大值
f=lambda *args:max(args) #单行函数
print(f(1,3,4,5,3,654,3,36,3,63,8,90))