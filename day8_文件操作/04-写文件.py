
#带w的，只要你操做了，就会清空文件
#如果文件不存在，会自动创建文件
# f=open('123.txt',mode='w',encoding='utf-8')
# f.write('123')
# f.close()

#a模式
# f=open('大戏吧',mode='a',encoding='utf-8')
# f.write('simida')
# f.flush()#强行把缓冲区中的内容放到磁盘中
# f.close()

#rb,wb,ab,处理的是非文本文件,mode里如果有b，就不能写encoding了
# f=open("c:/123.png",mode='rb')  #这里不能写encoding
# e=open('e:/123.png',mode='wb')
# for line in f:    #从c盘读取   line不知道读取了多少数据
#     e.write(line)  #写入e盘
# f.close()
# e.flush()
# e.close()