"""
udp 客户端流程
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 创建与服务端相同类型套接字
udp_sock = socket(AF_INET,SOCK_DGRAM)

# 循环发送接收
while True:
    msg = input(">>")
    if not msg:
        break  # 输入为空直接结束
    udp_sock.sendto(msg.encode(),ADDR)
    # if msg == "##":
    #     break # 告知服务器后，客户端结束
    data,addr = udp_sock.recvfrom(1024)
    print(data.decode())

udp_sock.close()
