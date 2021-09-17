"""
select 方法   select 函数
"""
from select import select
from socket import *

# 创建一些IO对象作为监控使用
tcp = socket()
tcp.bind(("0.0.0.0",8888))
tcp.listen(5)

udp = socket(type=SOCK_DGRAM)

print("开始监控....")
rs,ws,xs = select([tcp,udp],[udp],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)

