"""
基于epoll 的网络并发模型
"""
from socket import *
from select import *

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 创建一个监听套接字
sock = socket()
sock.bind(ADDR)
sock.listen(5)
sock.setblocking(False) # 设置为非阻塞IO

# 创建epoll对象
ep = epoll()
ep.register(sock,EPOLLIN)

# 建立查找字典 {fileno:object}
map = {sock.fileno():sock}

# 循环监控IO的发生
while True:
    events = ep.poll()
    # 通过遍历返回值列表确认是哪个IO对象就绪
    for fd,event in events:
        if fd == sock.fileno():
            # 监听套接字读事件处理
            conn,addr = sock.accept()
            print("Connect from",addr)
            conn.setblocking(False)
            ep.register(conn,EPOLLIN) # 加入客户端连接套接字
            map[conn.fileno()] = conn # 维护字典
        else:
            # 连接套接字读事件处理
            data = map[fd].recv(1024)
            if not data:
                ep.unregister(fd) # 不再关注
                map[fd].close()
                del map[fd] # 从字典删除
                continue
            print(data.decode())
            map[fd].send(b"OK")




