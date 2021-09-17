"""
block_io.py
非阻塞IO演示
"""
from socket import *
from time import sleep,ctime

log = open("my.log",'a',buffering=1) # 打开一个文件

# 监听套接字
sock = socket()
sock.bind(("0.0.0.0",8881))
sock.listen(5)

# 设置套接字为非阻塞IO -》sock调用所有函数都不阻塞
# sock.setblocking(False)

# 设置超时时间
sock.settimeout(2)

while True:
    try:
        conn,addr = sock.accept()
        print("Connect from",addr)
    except BlockingIOError as e:
        # 做与accept无关的事情
        sleep(2)
        msg = "%s : %s\n"%(ctime(),e)
        log.write(msg)
    except timeout as e:
        msg = "%s : %s\n" % (ctime(), e)
        log.write(msg)
    else:
        data = conn.recv(1024)
        print(data.decode())