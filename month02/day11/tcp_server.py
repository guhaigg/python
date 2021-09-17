"""
tcp 服务端流程
重点代码 ！！
长连接形态
"""
from socket import *

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听
tcp_socket.listen(5)

# 循环处理客户端连接
while True:
    print("等待连接....")
    conn,addr = tcp_socket.accept()
    print("连接：",addr)

    # 先收后发
    while True:
        data = conn.recv(1024)
        # 两种结束情况 客户端退出   客户端指令##
        if not data or data == b"##":
            break
        print("收到:",data.decode())
        conn.send(b"Thanks")
    conn.close()

# 关闭套接字
tcp_socket.close()


