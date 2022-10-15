# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        # 等待浏览器访问
        conn, addr = sock.accept()
        # 接收浏览器发送来的请求内容
        data = conn.recv(1024)
        print(data)

        # 给浏览器返回内容
        conn.send(b"HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send("电脑前的你长的真好看!".encode("utf-8"))

        # 关闭和浏览器创建的socket连接
        conn.close()


if __name__ == "__main__":
    main()