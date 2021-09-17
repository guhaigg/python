"""
练习： 假设在客户端有一张照片，请使用tcp
上传到服务端，在服务端以 20210909.jpeg 保存

plus : 假设文件比较大，不宜一次行读取全部内容

思路： 读取数据 发送
      接收数据 写入
"""
from socket import *

# 做事 : 收一个文件
def handle(conn):
    fw = open("../day11/20210909.jpeg", 'wb')
    while True:
        data = conn.recv(1024)
        if data == b'##':
            break # 对方发送完成直接退出得到空字串
        fw.write(data)
    fw.close()
    conn.send("您已上传成功".encode())

# 搭建网络模型
def main():
    # 创建监听套接字
    sock = socket()
    sock.bind(("0.0.0.0",8888))
    sock.listen(5)
    # 循环接收连接
    while True:
        conn,addr = sock.accept()
        print("Connect from",addr)
        handle(conn)  # 具体的文件处理
        conn.close()

if __name__ == '__main__':
    main()









