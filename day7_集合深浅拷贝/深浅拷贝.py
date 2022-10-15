
#必须引入copy模块
import copy
lst1=["金毛狮王","紫衫龙王","轻易父王","白眉鹰王",["张无忌"]]

#lst2=lst1  #把地址赋值给它
#lst2=lst1[:]  #切片会产生新的列表   #浅拷贝
# lst2=lst1.copy()  #浅拷贝
lst2=copy.deepcopy(lst1)
lst1[4]=lst1.append("小昭")
print(lst1)
print(lst2)
print(id(lst1))
print(id(lst2))

#1.赋值操作，没有创建新的对象
#2.浅拷贝，只拷贝第一层内容： [:]   copy()
#3.深拷贝，把这个对象内部的内容全部拷贝一份   ，引入copy模块。 deepcopy()
