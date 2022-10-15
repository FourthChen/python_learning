# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 18:47
# @Author  : sihao
# @File    : server.py

import socket
import json
import struct
import hashlib
sock=socket.socket()

sock.bind(("127.0.0.1",8001))

sock.listen(5)

while 1:
    print("server is working....")
    conn,addr=sock.accept()
    while 1:
        #接受json的打包长度
        file_info_json_pack=conn.recv(4)
        file_info_length=struct.unpack("i",file_info_json_pack)[0]

        #接受json字符串
        file_info_json=conn.recv(file_info_length).decode("utf8")
        file_info=json.loads(file_info_json)

        # 文件信息
        action = file_info.get('action')
        filename = file_info.get('filename')
        filesize = file_info.get('filesize')


        # 循环接受文件数据\
        md5=hashlib.md5()
        with open("put/" + filename, 'wb') as f:
            recv_data_length = 0
            while recv_data_length < filesize:
                data = conn.recv(1024)
                recv_data_length += len(data)
                f.write(data)
                #MD5摘要
                md5.update(data)
                print('文件总大小：%s,已成功接受%s' % (filesize, recv_data_length))

        print("接受成功")
        conn.send(b"ok")
        print(md5.hexdigest())
        val_md5=md5.hexdigest()
        md5_val=conn.recv(1024).decode("utf8")
        if val_md5==md5_val:
            print("校验成功")
        else:
            print("校验失败")