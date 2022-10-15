
# class foo:
#     def __init__(self,name):
#         self.name=name
#         self.age=123
#     def func(self):
#         print(self.name)
# obj=foo('章盖月')
# print(obj.name)
# print(obj.age)
# obj.func()

class foo:
    def __init__(self,name):
        #私有的实例变量（私有字段）
        self.__name=name #私有变量
        self.age=123
    def func(self):
        print(self.__name)
obj=foo('章盖月')
print(obj.age)
obj.func()