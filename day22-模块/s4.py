
"""
完成以下功能
    老狗/20岁/男/上山去砍柴
    老狗/20岁/男/开车去东北
    老狗/20岁/男/喜欢大保健
"""
# class Laogou:
#     def __init__(self,name,gender,age):  #特殊的方法，如果类名后边加括号，则该方法被立即执行
#         self.n1=name
#         self.n2=age
#         self.n3=gender
#     def kc(self):
#         data="%s,性别:%s,今年%s岁，喜欢上山砍柴"%(self.n1,self.n3,self.n2)
#         print(data)
#
#     def db(self,name,age,gender):
#         data="%s,性别:%s,今年%s岁，喜欢开车去东北"%(name,gender,age)
#         print(data)
#
#     def bj(self,name,age,gender):
#         data="%s,性别:%s,今年%s岁，喜欢大宝剑"%(name,gender,age)
#         print(data)
# obj=Laogou('老狗',20,'男')
# print(obj.n1)

# obj.kc('老狗',20,'男')
# obj.db('老狗',20,'男')
# obj.bj('老狗',20,'男')

class FileHandler:
    def __init__(self,file_path):
        self.file_path=file_path
    def read_first(self):
        pass
    def read_last(self):
        pass
