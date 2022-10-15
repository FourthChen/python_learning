import socket

client=socket.socket()
server_ip_port=("127.0.0.1",8510)
client.connect(server_ip_port)
while 1:
    msg=input("请输入你的指令>>>")
    client.send(msg.encode("utf-8"))

    from_server_stdout=client.recv(1024).decode("utf-8")
    from_server_error=client.recv(1024).decode("utf-8")

    print("收到的正确信息>>>",from_server_stdout)
    print("收到的错误信息>>>",from_server_error)
client.close()