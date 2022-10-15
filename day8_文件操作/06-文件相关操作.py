
# f =open('123.txt',mode='r',encoding='utf-8')
# # # # for line in f:
# # # #     print(line.strip())
# # # # f.seek(0)
# # # # for line in f:
# # # #     print(line.strip())
# # # # f.close()

f =open('123.txt',mode='r',encoding='utf-8')
f.seek(3)  # 3个type  ==一个汉字
s=f.read(1)  #读取一个字符
print(f.tell())  #tell() 告诉我光标在哪
f.close()

#seek（偏移量，位置）
# seek(0)  开头
# seek(0,2)  #在末尾的偏移量是0，末尾
#truncate()    删除光标后的内容