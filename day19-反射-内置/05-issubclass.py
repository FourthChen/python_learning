
class animal:
    pass

class cat(animal):
    pass

class bo_si_cat(cat):
    pass

print(issubclass(cat,animal)) #判断cat是 animal的子类
print(issubclass(bo_si_cat,animal))#Ture