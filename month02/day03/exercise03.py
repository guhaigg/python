"""
编写一个程序,循环不停的写入日志 (my.log)。
每2秒写入一行,要求每写入一行都要显示出来。
格式:  1. Mon Aug 30 17:00:08 2021
      2. Mon Aug 30 17:00:10 2021
      3. Mon Aug 30 17:13:22 2021
      4. Mon Aug 30 17:13:24 2021
结束程序后（强行结束）,重新运行要求继续往下写，
序号衔接
提示: time.ctime() 获取当前时间
     time.sleep() 间隔
"""
import time

# 每行实时显示  a --> 文件偏移量结尾
log = open("my.log",'a+',buffering=1)

log.seek(0,0) # 文件偏移量放到开头
# n = 现有的行数 + 1
n = len(log.readlines()) + 1
while True:
    msg = "%d. %s\n"%(n,time.ctime())
    log.write(msg)
    time.sleep(2) # 时间间隔2s
    n += 1





