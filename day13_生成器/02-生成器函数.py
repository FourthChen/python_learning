
# def func():
#     print('哈哈')
#     yield  1   #return和yield都可以返回数据
#     print('hehe')
#
# gen=func()  #不会执行你的函数，拿到的是生成器


#函数如果有yield，这个函数就是生成器函数，生成器函数(),获取的是生成器，这个时候不执行函数
#yield:  相当于return  可以返回数据，但是yield不会彻底中断函数，分段执行函数

# gen.__next__()#执行函数，执行到下一个yield
# gen.__next__() #继续执行函数到下一个yield

# def order():
#     lst=[]
#     for i in range(10000):
#         lst.append('衣服' + str(i))
#     return lst
# ll=order()
#下面程序的内存消耗小
# def order():
#     lst=[]
#     for i in range(10000):
#         yield '衣服'+str(i)
#
# ll=order()  #获取生成器
# ming=ll.__next__()
# print(ming)
# yi=ll.__next__()
# print(yi)

#send()  和__next()__是一样的，可以执行到下一个yield，可以给上一个yield位置传值
# def func():
#     print('我是第一段')
#     a=yield 123
#     print(a)
#     print('我是第二段')
#     b=yield 456
#     print(b)
#     print('我是最后一段')
#     c=yield 789   #最后收尾一定是yield
#
#
# g=func()
# print(g.__next__())#没有上一个yield 所以不能使用send() 开头必须是__next()__
# print(g.send("zzz"))
# print(g.__next__())

def func():
    yield 1
    yield 2
    yield 3
    yield 4
for i in func():  #for的内部一定有__next__()
    print(i)
print(list(func()))#内部都有__next__()

