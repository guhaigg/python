"""
基于多进程的tcp网络并发模型 --> 函数
重点代码 ！！！
"""
from multiprocessing import Process
from socket import *

# 服务器地址信息
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


# 客户端处理函数
def handle(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        conn.send(b"OK")
    conn.close()


# 搭建网络
def main():
    # 创建监听套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %d"%PORT)
    # 循环处理客户端连接
    while True:
        try:
            conn, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sock.close()
            break
        # 为每个客户端创建独立的进程处理客户端请求
        p = Process(target=handle, args=(conn,),daemon=True)
        p.start()

if __name__ == '__main__':
    main()