
import socket
#创建服务端socket对象
server=socket.socket()

#绑定IP和端口
server.bind(('10.104.3.215',8001))

#后边可以等5个人
server.listen(5)

print('服务端开始准备接受客户端的连接')

#等待客户端来链接,如果没人来就傻傻的等待
#coon是客户端和服务端连接的对象（伞），服务端以后要通过该对象进行收发数据
#addr是客户端的地址信息
#阻塞，只有有客户端连接，则后去客户端连接然后开始进行通信
coon,addr=server.accept()#######################在此会阻塞
#print('有人来连接了',coon,addr)

#通过对象去获取(王晓东通过伞给我发送消息)
#1024表示，服务端通过（伞）获取数据时，一次性最多拿1024字节
data=coon.recv(1024)
print(data)

#服务器通过连接对象（伞）给客户端回复了一个消息
coon.send(b'stop')

#与客户端断开连接（放开那把伞）
coon.close()

#关闭服务端的服务
server.close()
