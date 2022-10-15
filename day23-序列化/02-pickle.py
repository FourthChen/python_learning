import pickle

# dumps 序列化  把对象转化为bytes
# loads  反序列化  把bytes转化为对象
# dump  序列化  把对象转化成bytes并写入文件
# load  反序列化  把文件中的bytes读取，转换成对象

class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def catch_mouse(self):
        print(self.name,self.age,"抓老鼠")


c=cat("jerry",18)
# c.catch_mouse()
#
# #dump 把对象转化为bytes
# bs=pickle.dumps(c)
# print(bs)
#
# #把bytes 转换回对象   反序列化
# ccc=pickle.loads(bs)
# ccc.catch_mouse()

# dic={"jay":"周杰伦","jj":"林俊杰"}
# bs=pickle.dumps(dic)
# print(bs)
#
# d=pickle.loads(bs)
# print(d)

c=cat("jerry",18)
f=open("pickle-test",mode="wb")
pickle.dump(c,f)  #人是看不了的
f.close()