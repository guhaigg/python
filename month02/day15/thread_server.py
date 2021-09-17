"""
基于线程 的tcp网络并发模型 --》 class
重点代码 ！！！
"""
from socket import *
from threading import Thread


class Handle(Thread):
    def __init__(self, conn):
        self.conn = conn
        super().__init__(daemon=True)

    # 处理客户端请求
    def run(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            print(data.decode())
            self.conn.send(b"OK")
        self.conn.close()


# 搭建网络模型
class TCPServer:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self._create_socket()

    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        return sock

    # 启动服务
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)
        # 循环连接客户端
        while True:
            conn, addr = self.sock.accept()
            print("Connect from", addr)
            # 为客户端生成线程 -->自定义线程类
            t = Handle(conn)
            t.start()


if __name__ == '__main__':
    server = TCPServer(host="0.0.0.0", port=8888)  # 启动服务前的准备
    server.serve_forever()  # 启动服务
