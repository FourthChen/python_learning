# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 22:10
# @Author  : sihao
# @File    : 01-udp发送数据.py
import socket
def main():
    #创建一个udp套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #可以使用套接字收发数据
    #udp_socket.sendto(消息,对方ip及端口号)
    udp_socket.sendto(b"hahahah",())
    #关闭套接字
    udp_socket.close()
if __name__=='__main__':
    main()