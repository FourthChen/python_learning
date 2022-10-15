
class foo:
    def __init__(self,name):
        self.name=name

    def chi(self):
        print("人喜欢吃东西%s"%self.name)

p=foo('刘伟')

val=input("请输入你想让刘伟执行的操作:")
if hasattr(p,val):
    chi=getattr(p,"chi")
    chi()


#补充
#把chi（）函数换成lambda
setattr(master,'chi',lambda x:x+1)