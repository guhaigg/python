from socket import *
from time import sleep

stu=[
    "Tom:18:89",
    "Lily:17:88",
    "Jame:18:90"
]
sock = socket()
sock.connect(("127.0.0.1",8888))

# 循环发送内容 最后 ##  表示发送完毕
for row in stu:
    sock.send((row+"\n").encode()) # 增加消息边界
sleep(0.1) # 发送延迟
sock.send(b"##")


# sock.send(b"Hello world")

sock.close()