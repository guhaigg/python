"""
重点练习 !!!
编写一个函数,完成一个文件的复制
函数参数传入一个文件(文件类型不确定),传入的值可以代
路径,执行函数将该文件复制一份,到程序所在目录下

思路 : 从源文件读取 --> 向新文件写入
"""
def copy(filename):
    fr = open(filename,'rb')
    new = filename.split('/')[-1] # 文件名
    fw = open(new, 'wb')

    # fw.write(fr.read()) # 一次性读取,不适合大文件

    # 循环读写,所有大小的文件都可以
    while True:
        data = fr.read(1024)  # 读
        if not data:
            break # 文件结尾结束循环
        fw.write(data)  # 写

    fr.close()
    fw.close()


copy("/home/tarena/下载/sun.jpeg")