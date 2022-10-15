import socket

client=socket.socket()
server_ip_port=("127.0.0.1",8500)
client.connect(server_ip_port)

client.send('hello'.encode("utf-8"))
client.send("sigiu".encode("utf-8"))