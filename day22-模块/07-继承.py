# class ba:  #父类，基类
#     def f2(self):
#         print('f2')
# class foo(ba):  #子类，派生类
#     def fi(self):
#         print("f1")
#
# obj=foo()
# obj.fi()
# obj.f2()
#原则：现在自己类找，没有就在父类中找

#####为何要有继承

# class foo:
#     def f1(self):
#         pass
# class f(foo):
#     def f2(self):
#         pass
# class o(foo):
#     def f3(self):
#         pass


##############2.多继承###################
'''
class b1:
    def show(self):
        print("b1")
class b2:
    def show(self):
        print("b2")
class b3(b1,b2):
    pass

obj=b1()
obj.show()
'''


class base:
    def f1(self):
        print('f1')
class foo(base):
    def f2(self):
        print('f2')

# obj=foo()
# obj.f2()
# obj.f1()
obj=base()
obj.f1()
obj.f2()  #不会在儿子里找，只能在父类里找