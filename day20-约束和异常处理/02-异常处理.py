
#程序运行过程中产生的错误，不正常
# def chufa(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as e:
#         print("出错了，0不能当 除数")
# ret=chufa(10,0)
# print(ret)


#计算两个整数的加法
# def add(a,b):
#     if type(a)!=int or type(b)!=int:
#         return TypeError("我只要整数")
#     return a+b
#
# ret=add(2.2,2)
# print(ret)

class GenderError(Exception):
    pass