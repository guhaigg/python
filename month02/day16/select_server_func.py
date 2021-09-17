"""
基于select 的IO多路复用并发网络模型
"""
from socket import *
from select import select

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# IO多路复用的关注列表
rlist = []
wlist = []
xlist = []


# 创建监听套接字
def create_socket():
    # 创建一个监听套接字
    sock = socket()
    sock.bind(ADDR)
    sock.setblocking(False)  # 设置为非阻塞IO
    return sock


def connect_client(sock):
    # 监听套接字读事件处理
    conn, addr = sock.accept()
    print("Connect from", addr)
    conn.setblocking(False)
    rlist.append(conn)  # 加入客户端连接套接字


# 处理客户端
def handle(conn):
    # 连接套接字读事件处理
    data = conn.recv(1024)
    if not data:
        rlist.remove(conn)  # 不再关注
        conn.close()
        return
    print(data.decode())
    conn.send(b"OK")


def main():
    sock = create_socket()
    sock.listen(5)
    print("Listen the port %d" % PORT)
    rlist.append(sock)  # 初始关注
    # 循环监控IO的发生
    while True:
        rs, ws, xs = select(rlist, wlist, xlist)
        # 通过遍历返回值列表确认是哪个IO对象就绪
        for r in rs:
            if r is sock:
                connect_client(r)
            else:
                handle(r)

if __name__ == '__main__':
    main()