"""
文件写操作示例 write_file

每次写入都从上次结尾开始,需要自己添加格式控制
"""
# 写方式打开
# file = open("file.txt",'w')
# file = open("file.txt",'wb') # 二进制  写入字节串
file = open("file.txt",'a') # 追加

# 写入内容
# n = file.write("Hello,死鬼\n")
# print("n =",n)
# n = file.write("哎呀,干哈?\n")
# print("n =",n)

# 列表中每一项分别写入
data = ["小明\n","小刚\n","小妹"]
file.writelines(data)


# 关闭
file.close()
