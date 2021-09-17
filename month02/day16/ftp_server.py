"""
ftp文件服务器  服务端
并发网络模型训练
"""
from socket import *
from threading import Thread
import os
from time import sleep

# 文件库
FTP = "/home/tarena/FTP/"


# 具体处理用户请求
class Handle(Thread):
    def __init__(self, conn):
        self.conn = conn
        super().__init__(daemon=True)

    # 处理客户端请求
    def run(self):
        # 循环接收请求分情况讨论
        while True:
            request = self.conn.recv(1024).decode()
            tmp = request.split(' ')  # 提取请求类型
            if not request or request == "QUIT":
                break
            elif request == "LIST":
                self.do_list()
            elif tmp[0] == "GET":
                self.do_get(tmp[1])  # [GET,filename]
            elif tmp[0] == "PUT":
                self.do_put(tmp[1])  # [PUT,filename]
        self.conn.close()

    def do_list(self):
        files = os.listdir(FTP) # 获取文件列表
        if files:
            self.conn.send(b"OK")
            sleep(0.1)
            # 发送文件列表 data->"file1\nfile2.."
            data = '\n'.join(files)
            self.conn.send(data.encode()) # 一次发送
        else:
            self.conn.send(b"FAIL")

    def do_get(self, filename):
        try:
            fr = open(FTP + filename, "rb")
        except:
            self.conn.send(b"FAIL")
        else:
            self.conn.send(b"OK")
            sleep(0.1)
            while True:
                data = fr.read(1024)
                if not data:
                    break
                self.conn.send(data)
            fr.close()
            sleep(0.1)
            self.conn.send(b"##")

    def do_put(self, filename):
        if os.path.exists(FTP + filename):
            self.conn.send(b"FAIL")
        else:
            self.conn.send(b"OK")
            fw = open(FTP + filename, 'wb')
            while True:
                data = self.conn.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()


# 搭建网络模型
class FTPServer:
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
    ftp = FTPServer(host="0.0.0.0", port=8888)  # 启动服务前的准备
    ftp.serve_forever()  # 启动服务
