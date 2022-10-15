
import socket

sock=socket.socket()
sock.connect(('127.0.0.1',8899))

while 1:
    user=input('用户名>>>')
    pwd=input('密码>>>')
    val=('%s|%s'%(user,pwd)).encode('utf-8')
    sock.send(val)
    reponse=sock.recv(1024)
    print(reponse.decode('utf-8'))
    if reponse.decode('utf-8')=='success':
        break
    else:
        print('用户名或者密码错误')
        continue