"""
udp服务端流程
重点代码 ！！
"""
from socket import *

# 创建udp套接字
udp_sock = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
udp_sock.bind(("0.0.0.0",8888))


# 先收后发
while True:
    data,addr = udp_sock.recvfrom(5)
    # 服务器程序往往长期执行不退出
    # if data == b"##":
    #     break  # 得到通知退出
    print(addr,":",data.decode())
    udp_sock.sendto(b'Thanks',addr)

# 关闭套接字
udp_sock.close()



