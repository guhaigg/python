"""
有一个大文件，将其拆分成上下两个部分 （按照字节大小），
要求两个部分拆分要同步进行
plus ： 假设文件很大不要一次read读取全部
os.path.getsize()
"""
import os
from multiprocessing import Process

# 复制上半部分
def top(filename):
    fr = open(filename,'rb')
    fw = open("top.jpeg",'wb')
    n = os.path.getsize(filename) // 2
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot(filename):
    fr = open(filename, 'rb')
    fw = open("bot.jpeg", 'wb')
    n = os.path.getsize(filename) // 2
    fr.seek(n) # 文件偏移量到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()


def main():
    jobs = []
    for func in [top,bot]:
        p = Process(target=func,args=("/home/tarena/下载/bizhi.jpeg",))
        jobs.append(p)
        p.start()
    [i.join() for i in jobs] # 和循环一个意思 酷
    print("文件拆分完成")

if __name__ == '__main__':
    main()








