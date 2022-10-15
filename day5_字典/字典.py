# dic ={ 'name':'alex','age':9000}   #字符串
# print(dic)

# dic = { 1:'a',2:'b',3:'c'}  # 数字
# print(dic)

# dic = { True:'1', False:'0'}    #布尔值
# print(dic)

# dic ={ (1,2,3):'abc'}  #元组
# print(dic)

# dic ={ [1,2,3]:'abc'}  # 列表
# print(dic)

# dic ={'易大师':'剑圣','剑豪':'托儿所'}
#增
# dic ['诺手'] = '人头狗'  # 新增
# print(dic)

# dic.setdefault('火女','安妮')  #若在字典中存在就不进行任何操作
#                                #不存在就进行添加
# print(dic)

#删
# pop
# ret=dic.pop('易大师')  #通过key删除   返回被删除的value
# print(ret)
# del
# del dic ['易大师']
# print(dic)
# clear
# dic.clear()   #{}
# print(dic)
#
# ret =dic.popitem()  #随机删除  返回值： 一个元组 （key，value）
# print(ret)
# # 字典没有remove

# 改：
# dic ['剑豪']='哈啥给'  #强制修改
# print(dic)

# dic1 ={'火女':'安妮','火男':'布塄德'}
# dic.update(dic1)   #把dic1 添加到dic中
# print(dic)

#查
# for 循环
# for i in dic:
#     print(i)    #for循环默认是获取字典中的健
#
# print(dic['易大师'])   #查看1   没有这个健时查询会报错
# print(dic.get('易大3师','你傻啊，没有'))   #没有返回none 可以指定返回内容

# print(dic.setdefault('易大师'))  #查找   没有返回none

#字典中独特的方法
#keys value  item
# print(dic.keys())  #(高仿列表)
# print(dic.values())   #(高仿列表)
# for i in dic.keys():
#     print(i)    #获取到字典中的键
# for i in dic.values():
#     print(i)    #获取到字典中的值
# for i in dic.items():
#     print(i)    #

#解构  （解包）     将后边结构打开按位置赋值给变量  支持 字符串  列表 元组
# a,b=1,2
# print(a)
# print(b)
# a,b=(1,2)   #将后面结构打开按位置赋值给变量
# print(a)
# print(b)
# a,b=[1,2]   #将后面结构打开按位置赋值给变量
# print(a)
# print(b)
# for i in dic.items():
#     a,b=i
#     print(a)
#     print(b)         #元组解包
# for a,b in dic.items():
#     print(a)
#     print(b)         #元组解包

#字典的嵌套
dic = {
    'name':'汪峰',
    'age':43,
    'wife':{
        'name':'章子怡',
            'age':39,
            'salary':1000
            },
        'baby':{
            'name':'熊大','age':18
        }
}
print(dic['baby']['age'])