import socket
import subprocess
server=socket.socket()
ip_port=("127.0.0.1",8510)
server.bind(ip_port)

server.listen()
conn,addr=server.accept()
while 1:
    #来自客户端的指令
    from_client_cmd=conn.recv(1024).decode("utf-8")
    sub_obj=subprocess.Popen(
        from_client_cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    server_cmd_msg=sub_obj.stdout.read().decode("gbk")
    server_cmd_err=sub_obj.stderr.read().decode("gbk")

    print("指令返回的正确信息>>>",server_cmd_msg)
    print("指令返回的错误信息>>>",server_cmd_err)
    conn.send(server_cmd_msg.encode("utf-8"))
    conn.send(server_cmd_err.encode("utf-8"))
server.close()