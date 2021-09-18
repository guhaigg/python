"""
http 请求 响应
"""
from socket import *

sock = socket()
sock.bind(("0.0.0.0",8888))
sock.listen(5)

# 等待浏览器连接
conn,addr = sock.accept()
print("Connect from",addr)

# 收到浏览器自动发送的http请求
data = conn.recv(1024)
print(data.decode())

# 组织响应格式
response = """HTTP/1.1 200 OK
Content-Type:text/html

Hello world
"""
conn.send(response.encode()) # 发送响应

conn.close()
sock.close()