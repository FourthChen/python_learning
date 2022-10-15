import socket

sock=socket.socket()  #TCP协议
IP_PORT=('127.0.0.1',8899)
sock.bind(IP_PORT)
sock.listen(5)
while 1:
    conn,addr=sock.accept()
    data=conn.recv(1024).decode('utf-8')
    print('接受信息：',data)
    user,pwd =data.split('|')

    #文件操作
    flag=False
    with open('account','r') as f:
        for line in f:
            print('===')
            username,password=line.strip().split(':')
            if username==user and password==pwd:
                flag=True
                break
    if flag:
        conn.send(b'success')
    else:
        conn.send(b'fail')