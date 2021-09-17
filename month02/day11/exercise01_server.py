"""
练习01 ： 使用udp完成一个查单词程序
利用words数据表完成，在客户端输入一个单词
发送给服务端，从服务端接收回复回来的单词解释，
在客户端打印出来
"""
import pymysql
from socket import *


# 数据库处理类
class Dict:
    def __init__(self):
        self.kwargs = {
            "user": "root",
            "password": "123456",
            "database": "dict",
            "charset": "utf8"
        }
        self.db = pymysql.connect(**self.kwargs)
        self.cur = self.db.cursor()

    def close(self):
        # 关闭数据库
        self.cur.close()
        self.db.close()

    def get_mean(self, word):
        sql = "select mean from words where word=%s;"
        self.cur.execute(sql, [word])
        result = self.cur.fetchone()  # (mean,) None
        if result:
            return result[0]
        else:
            return "Not Found"  # 没有这个单词


# 网络通信 --》 收单词  发解释
class DictServer:
    def __init__(self, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.dict = Dict()  # 跨类调用
        self.sock = self._create_socket()

    def _create_socket(self):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.bind(self.address)
        return sock

    # 具体干的事情
    def query_word(self):
        while True:
            word, addr = self.sock.recvfrom(128)
            # 获取到解释
            mean = self.dict.get_mean(word.decode())
            self.sock.sendto(mean.encode(), addr)

    def close(self):
        self.dict.close()
        self.sock.close()


if __name__ == '__main__':
    dict = DictServer(host="0.0.0.0",port=8888)
    dict.query_word()
    dict.close()
