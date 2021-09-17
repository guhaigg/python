from socket import *

# 创建UDP套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

#  绑定地址
udp_socket.bind(("0.0.0.0",8888))

while True:
    # 接收发送消息  data--> bytes
    data,addr = udp_socket.recvfrom(5)
    if data == b"##":
        break
    print("从",addr,"收到:",data.decode())

    # 发送给刚才收到的地址
    udp_socket.sendto(b"Thanks",addr)

# 关闭套接字
udp_socket.close()