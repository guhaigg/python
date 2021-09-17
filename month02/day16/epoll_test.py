"""
epoll方法
"""
from select import *
from socket import *

# 创建一些IO对象作为监控使用
tcp = socket()
tcp.bind(("0.0.0.0",8888))
tcp.listen(5)

udp = socket(type=SOCK_DGRAM)

# 创建epoll对象
ep = epoll()

# 关注tcp读事件
ep.register(tcp,EPOLLIN)
ep.register(udp,EPOLLOUT)

# 查找字典：fileno() --> io object
map = {tcp.fileno():tcp,udp.fileno():udp}

print("开始监控....")
events = ep.poll()
print(events) # [(3, 1)]  3->tcp文件描述符

for fd,event in events:
    print(map[fd])

