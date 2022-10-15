# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 18:47
# @Author  : sihao
# @File    : client.py
import socket
import os
import json
import struct
import hashlib
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

    ret=struct.pack("i",len(file_info_json))
    #发送file_info_json的打包长度
    sock.send(ret)
    #发送file_info_json字节串
    sock.send(file_info_json)
    #发送文件数据
    md5=hashlib.md5()
    with open(filename,'rb') as f:
        for line in f:
            sock.send(line)
            md5.update(line)
    data=sock.recv(1024)
    print(data)
    print(md5.hexdigest())
    val_md5=md5.hexdigest()
    sock.send(val_md5.encode("utf8"))