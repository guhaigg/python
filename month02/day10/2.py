from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 与服务端相同套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 发送消息
while True:
    msg = input(">>")
    if not msg:
        break

    udp_socket.sendto(msg.encode(),ADDR)
    # 结束发送
    # if msg == "##":
    #     break

    data,addr = udp_socket.recvfrom(128)
    print("从服务端收到:",data.decode())

udp_socket.close()