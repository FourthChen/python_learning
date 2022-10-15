# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 18:47
# @Author  : sihao
# @File    : client.py
import socket
import os
import json
sock=socket.socket()

sock.connect(("127.0.0.1",8001))

while 1:
    cmd=input("请输入命令：") #put 123.jpg

    action,filename=cmd.strip().split(" ")
    filesize=os.path.getsize(filename)
    file_info={
        "action":action,
        "filename":filename,
        "filesize":filesize
    }
    #由于只能发送字节，因此需要用json序列化
    file_info_json=json.dumps(file_info).encode("utf8")
    sock.send(file_info_json)

    #确认服务端收到了文件信息
    code=sock.recv(1024).decode('utf8')
    if code=='200':
        #发送文件数据
        with open(filename,'rb') as f:
            for line in f:
                sock.send(line)
    else:
        print("异常")