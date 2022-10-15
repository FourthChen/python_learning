#无论你读取了多少内容，光标在哪，写入的时候都是在结尾写入
#最好用的读写同时存在的模式
#r+  读写模式  先读后写
#w+  写读模式  先写后读
# f =open('123.txt',mode='r+',encoding='utf-8')
# # s=f.read(3)#读取三个字符
# # print(s)
# # f.write('buyangle')
# # f.close()

f =open('123.txt',mode='w+',encoding='utf-8')
f.write('zhang')  #写完之后光标在最后，读取是灭有内容的
f.seek(0)#  移动光标到开头
s=f.read()
print(s)
f.flush()
f.close()
