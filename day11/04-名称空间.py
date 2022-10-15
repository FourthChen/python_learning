
# print('哈哈')
# print('呵呵')

# a=10  #全局名称空间中的内容
# def fn():   #fn也在全局名称空间
#     b=20  #  局部名称空间
#     print(a)
# def gn():
#     print(a)
# fn()
# gn()

#1.内置  2.全局  3.局部（函数调用）

a=10 #全局
def fn():
    b=20  #局部
    def gn():   #局部
        pass
def en():
    pass
print(globals())  #可以查看全局作用域中的内容
print(locals())   #查看当前作用域的内容
