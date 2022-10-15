
import socket
import struct
sock=socket.socket()
sock.connect(('127.0.0.10',8009))

while 1:
    cmd=input('请输入命令>>>')
    sock.send(cmd.encode("utf-8"))
    if cmd =="":
        continue
    if cmd=="exit":
        break

    header_pack=sock.recv(4)
    data_length=struct.unpack("i",header_pack)[0]
    print("data_length",data_length)

    recv_data_length=0
    recv_data=b''
    while recv_data_length<data_length:
        data=sock.recv(1024)
        recv_data_length+=len(data)
        recv_data+=data
    print(recv_data.decode("gbk"))

sock.close()