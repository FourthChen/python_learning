

class animal:
    pass

class cat(animal):
    pass

class bo_si_cat(cat):
    pass

a=animal()
print(isinstance(a,animal)) #自己的类可以判断
print(isinstance(a,cat))  #子类不能判断

#isinstamce 判断的是对象是否是xxx家族里的内容，网上找
c=bo_si_cat()
print(isinstance(c,animal))
print(isinstance(c,cat))


lst=[1,2,3,4]
print(lst.__iter__())  #拿它的迭代器