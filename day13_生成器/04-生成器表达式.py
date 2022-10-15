
# tu=(i for i in range(10))  #没有元组推导式，叫做生成器表达式
# print(tu)  #生成器
# print(tu.__next__())
# print(tu.__next__())
# print(tu.__next__())

# lst=[i for i in range(10)]  #列表
# print(lst)
#
# gen=(i for i in range(10))  #生成器,惰性机制

#==================面试题=================
#生成器函数
# def func():
#     print(111)
#     yield 222
# g=func()     #获取生成器
#
# g1=(i for i in g)  #生成器
# g2=(i for i in g1)  #生成器
#
# print(list(g))  #[222]   源头，把数据拿走了
# print(list(g1))  #  []  这里执行的时候，源头已经没有数据了
# print(list(g2))  # [] 这里没有值了

#==================面试题======================
#求和
def add(a,b):
    return a+b
#生成器函数
def test():
    for r_i in range(4):
        yield r_i
g=test()  #获取生成器

for n in [2,10]:
    g=(add(n,i)  for i in g)
#到最后往里面放数据就好了
print(list(g)) #[20, 21, 22, 23]