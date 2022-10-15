
lst=[16,18,32,54,12,9]

# lst.sort()  #list的方法
# print(lst)

#内置函数中提供了一个通用的排序方案，sorted()
# a=sorted(lst)
# print(a)
#
# lst=['聊斋','西游记','三国演义','葫芦娃','水浒传','年轮']

# def func(s):
#     return len(s)
#key:排序方案，sorted函数内部都会把可迭代对象中的每一个元素拿出来交给后面你的key
#后面的key计算出一个数字，作为当前这个元素的权重，整个函数根据权重进行排序
# ll=sorted(lst,key=func)
# print(ll)

# lst=[
#     {'name':'汪峰','age':48},
#     {'name':'章子怡','age':38},
#     {'name':'alex','age':39}
# ]
# def func(el):
#     return el['name']
# aa=sorted(lst,key=func)
# print(aa)
a={1:2,3:4,4:3,2:1,0:0}

a1=sorted(a.items(),key=lambda a:a[1])
print(a1)

def func(c):
    return c[1]
ccc=sorted(a.items(),key=func)
print(ccc)