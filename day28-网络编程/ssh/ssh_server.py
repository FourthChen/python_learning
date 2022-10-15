import socket
import subprocess
sock=socket.socket()  #TCP协议
IP_PORT=('127.0.0.10',8009)
sock.bind(IP_PORT)
sock.listen(5)

while 1:
    print("server is working....")
    conn, addr = sock.accept()
    while 1:
        try:
            cmd=conn.recv(1024).decode("utf-8")
            if cmd==b'exit':
                break
            res=subprocess.Popen(cmd,
                             shell=True,
                             stderr=subprocess.PIPE,
                             stdout=subprocess.PIPE
            )
            out=res.stdout.read()
            err=res.stderr.read()
            print("out响应长度",len(out))
            print("err响应长度",len(err))
            if err:
                # 构建报头
                import struct

                header_pack = struct.pack("i", len(err))
                # 发送报头
                conn.send(header_pack)
                # 发送数据
                conn.send(err)
            else:
                #构建报头
                import struct
                header_pack=struct.pack("i",len(out))
                #发送报头
                conn.send(header_pack)
                #发送数据
                conn.send(out)
            print("stdout",res.stdout.read())
            print("stderr", res.stderr.read().decode("gbk"))
            conn.send(res.stdout.read()) #若为空则发不过去
        except Exception as e:
            break

    conn.close()