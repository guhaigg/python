"""
字节串学习

所有字符串都能转换为字节串   是
所有字节串都能转换为字符串   否
"""

#　ascii 字符 字节串
byte1 = b"Hello world"
print(type(byte1))
print(byte1)

# utf-8 字符 字节串   encode() str->bytes
byte2 = "你好".encode()
print(byte2)

# 字节串转换为字符串 decode()
print(byte2.decode())
print(b'\xe4\xbd\xd6\xe3\xa4\xbd'.decode())
