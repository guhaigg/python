"""
查单词
"""
from socket import *

# 服务器地址
ADDR = ("127.0.0.1",8888)

class DictClient:
    def __init__(self):
        # 创建与服务端相同类型套接字
        self.sock = socket(AF_INET,SOCK_DGRAM)

    def query_word(self):
        # 循环发送接收
        while True:
            word = input("Word:")
            if not word:
                break  # 输入为空直接结束
            self.sock.sendto(word.encode(),ADDR)
            # 得到解释
            mean,addr = self.sock.recvfrom(1024)
            print("%s : %s\n"%(word,mean.decode()))

    def close(self):
        self.sock.close()

if __name__ == '__main__':
    dict = DictClient()
    dict.query_word()
    dict.close()