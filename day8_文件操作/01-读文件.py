
#文件路径
    # 1.绝对路径，从磁盘的根目录寻找或者从互联网上寻找
    # 2.相对路径（用的多），相对于当前程序所在的文件夹
# f=open('123.txt',mode='r',encoding='utf-8')
# s=f.read()
# print(s)
# f.close()  #如果没有这句话，你在下面的程序中如果删除这个文件，就会报错

# f=open('123.txt',mode='r',encoding='utf-8')
# s=f.readline().strip() #一次读一行
# print(s)
# s=f.readline().strip() #一次读一行
# print(s)
# s=f.readline().strip() #一次读一行,strip()是去掉空格的函数
# print(s)
# f.close()

f=open('123.txt',mode='r',encoding='utf-8')
for line in f:   #文件是一个可迭代对象
    print(line)

f.close()