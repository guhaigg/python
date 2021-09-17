"""
随堂练习：
主目录下有一个  FTP目录，在当前位置也有一个FTP，
两个文件夹存在一些文件重名
编写一个程序，将主目录中FTP下的所有文件向
当前目录下的FTP中拷贝，但是遇到同名文件需要提示
是"替换"还是"跳过"，根据用户选择执行操作，
不重名的文件则不用提示直接复制过去即可

思路提示：子进程负责拷贝文件
        父进程做文件是否重名判断，接收用户输入指令
"""
from multiprocessing import Process,Queue
import os

old = "/home/tarena/FTP/"
new = "./FTP/"
q = Queue() # 消息队列，用于传递文件名

def copy():
    while True:
        filename = q.get() # 从消息队列获取名字
        if filename == '##':
            break # 文件已经拷贝完成
        fr = open(old+filename,'rb')
        fw = open(new+filename,'wb')
        while True:
            data = fr.read(1024)
            if not data:
                break
            fw.write(data)
        fr.close()
        fw.close()

def select_file():
    new_files = os.listdir(new) # 当前目录FTP下的文件
    for file in os.listdir(old):
        if file in new_files:
            print("已存在%s 1.替换  2.跳过"%file)
            cmd = input("请选择:")
            if cmd == "1":
                q.put(file) # 选择1 则也放入消息队列
        else:
            q.put(file) # 要拷贝的文件名放入消息队列
    q.put("##") # 子进程结束标志

def main():
    p = Process(target=copy)
    p.start()
    select_file() # 文件筛选

if __name__ == '__main__':
    main()
