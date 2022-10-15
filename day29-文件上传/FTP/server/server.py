# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 18:47
# @Author  : sihao
# @File    : server.py

import socket
import json
sock=socket.socket()

sock.bind(("127.0.0.1",8001))

sock.listen(5)

while 1:
    print("server is working....")
    conn,addr=sock.accept()
    while 1:
        data=conn.recv(1024).decode("utf8")
        file_info=json.loads(data)
        print("file_info:",file_info)#file_info: {'action': 'put', 'filesize': '123.jpg', 'filename': '123.jpg'}
        #文件信息
        action=file_info.get('action')
        filename=file_info.get('filename')
        filesize=file_info.get('filesize')
        conn.send(b'200')


        #接受文件数据
        with open("put/"+filename,'wb') as f:
            recv_data_length=0
            while recv_data_length<filesize:
                data=conn.recv(1024)
                recv_data_length+=len(data)
                f.write(data)
                print('文件总大小：%s,已成功接受%s'%(filesize,recv_data_length))

        print("接受成功")