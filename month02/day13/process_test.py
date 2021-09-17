"""
100000以内质数之和

在无阻塞的任务执行中，并不是创建的进程越多越好，
而是受到cpu硬件的制约
"""
import time
from multiprocessing import Process

# 判断一个数是否为质数
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2,num // 2 + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def process_1():
#     prime = [] # 存放所有质数
#     for i in range(1,100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime)) # 求和
#
# begin = time.time()
# process_1() # 用时： 12.56395149230957
# print("用时：",time.time() - begin)


class Prime(Process):
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

def process_10():
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(i,i+10000)
        jobs.append(p)
        p.start()
    [i.join() for i in jobs]

begin = time.time()
# process_4() # 用时: 7.694790363311768
process_10() # 用时: 6.956717252731323
print("用时:",time.time() - begin)





