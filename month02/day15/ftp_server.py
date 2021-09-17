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
            tmp = request.split(' ') # 提取请求类型
            if not request or request == "QUIT":
                break
            elif request == "LIST":
                self.do_list()
            elif tmp[0] == "GET":
                self.do_get(tmp[1]) # [GET,filename]
            elif tmp[0] == "PUT":
                self.do_put(tmp[1]) # [PUT,filename]
        self.conn.close()

    def do_list(self):
        pass

    def do_get(self,filename):
        try:
            fr = open(FTP + filename,"rb")
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


    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.conn.send(b"FAIL")
        else:
            self.conn.send(b"OK")
            fw = open(FTP+filename, 'wb')
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
######################### 服务端 ############################
from socket import *
from threading import Thread
import os
from time import sleep

# 文件库
FTP = "/home/tarena/FTP/"


# 处理客户端具体请求
class Handle:
    def __init__(self, connfd):
        self.connfd = connfd

    def do_list(self):
        filelist = os.listdir(FTP)
        if filelist:
            self.connfd.send(b"OK")
            sleep(0.1)
            # 发送文件列表
            files = "\n".join(filelist)
            self.connfd.send(files.encode())
        else:
            self.connfd.send(b"FAIL")

    def do_get(self, filename):
        try:
            file = open(FTP + filename, 'rb')
        except:
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            # 　发送文件
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.connfd.send(data)
            file.close()
            sleep(0.1)
            self.connfd.send(b"##")

    def do_put(self, filename):
        # 判断文件是否存在
        if os.path.exists(FTP + filename):
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            # 接收文件
            file = open(FTP + filename, 'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b"##":
                    break
                file.write(data)
            file.close()

    def request(self):
        while True:
            data = self.connfd.recv(1024).decode()
            # 分情况具体处理请求函数
            tmp = data.split(' ')
            if not data or tmp[0] == "EXIT":
                break
            elif tmp[0] == "LIST":
                self.do_list()
            elif tmp[0] == "GET":
                # tmp-> [GET,filename]
                self.do_get(tmp[1])
            elif tmp[0] == "PUT":
                self.do_put(tmp[1])


# 创建线程得到请求
class FTPThread(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle(connfd)
        super().__init__(daemon=True)

    # 接收客户端的请求
    def run(self):
        self.handle.request()
        self.connfd.close()


# 网络搭建
class ConcurrentServer:
    """
    提供网络功能
    """

    def __init__(self, *, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self.__create_socket()

    def __create_socket(self):
        tcp_socket = socket()
        tcp_socket.bind(self.address)
        return tcp_socket

    # 启动服务 --> 准备连接客户端
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)

        while True:
            connfd, addr = self.sock.accept()
            print("Connect from", addr)
            # 创建线程
            t = FTPThread(connfd)
            t.start()


if __name__ == '__main__':
    server = ConcurrentServer(host="0.0.0.0", port=8880)
    server.serve_forever()  # 启动服务

# git config --global http.postBuffer 524288000
#  git config --global http.sslVerify false
