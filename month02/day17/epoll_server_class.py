"""
基于epoll 的网络并发模型
"""
from socket import *
from select import *


class EpollServer:
    def __init__(self, *, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self._create_socket()
        self.ep = epoll()
        self.map = {}  # 查找字典

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        sock.setblocking(False)
        return sock

    def _connect(self):
        # 监听套接字读事件处理
        conn, addr = self.sock.accept()
        print("Connect from", addr)
        conn.setblocking(False)
        self.ep.register(conn, EPOLLIN)  # 加入客户端连接套接字
        self.map[conn.fileno()] = conn  # 维护字典

    def handle(self, fd):
        # 连接套接字读事件处理
        data = self.map[fd].recv(1024)
        if not data:
            self.ep.unregister(fd)  # 不再关注
            self.map[fd].close()
            del self.map[fd]  # 从字典删除
            return
        print(data.decode())
        self.map[fd].send(b"OK")

    # 启动服务进行监控
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        self.ep.register(self.sock, EPOLLIN)
        # 循环监控IO的发生
        while True:
            events = self.ep.poll()
            # 通过遍历返回值列表确认是哪个IO对象就绪
            for fd, event in events:
                if fd == self.sock.fileno():
                    self._connect()
                else:
                    self.handle(fd)


if __name__ == '__main__':
    ep = EpollServer(host="0.0.0.0", port=8888)
    ep.serve_forever()
