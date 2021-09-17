"""
100000以内质数之和

在无阻塞的任务执行中，线程由于GIL问题不能提高效率
"""
import time
from threading import Thread

# 判断一个数是否为质数
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2,num // 2 + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def thread_1():
#     prime = [] # 存放所有质数
#     for i in range(1,100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime)) # 求和
#
# begin = time.time()
# thread_1() # 用时： 12.515781879425049
# print("用时：",time.time() - begin)


class Prime(Thread):
    @staticmethod
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True

    def __init__(self,begin,end):
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        prime = []  # 存放所有质数
        for i in range(self.begin,self.end):
            if Prime.is_prime(i):
                prime.append(i)
        print(sum(prime))

def thread_10():
    jobs = []
    for i in range(1,100001,10000):
        t = Prime(i,i+10000)
        jobs.append(t)
        t.start()
    [i.join() for i in jobs]

begin = time.time()
# thread_4() # 用时: 12.594112157821655
thread_10() # 用时: 12.398741960525513
print("用时:",time.time() - begin)





