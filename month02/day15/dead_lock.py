"""
死锁现象演示
"""
from time import sleep
from threading import Thread,Lock

# 账户类
class Account:
    def __init__(self,id,balance,lock):
        self._id = id
        self._balance = balance
        self.lock = lock

    # 取钱
    def withdraw(self,amount):
        self._balance -= amount

    # 存钱
    def deposit(self,amount):
        self._balance += amount

    # 查看余额
    def getBalance(self):
        return self._balance


# 转账函数
def transfer(from_,to,amount):
    from_.lock.acquire()
    from_.withdraw(amount) # from_钱减少
    from_.lock.release() # 不会产生死锁
    sleep(0.1) # 网络延迟

    to.lock.acquire()
    to.deposit(amount) # to钱增加
    to.lock.release()
    # from_.lock.release()  # 会产生死锁


if __name__ == '__main__':
    tom = Account("Tom",5000,Lock())
    abby = Account("abby",8000,Lock())

    t1 = Thread(target=transfer,args=(tom,abby,600))
    t2 = Thread(target=transfer,args=(abby,tom,400))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Tom:",tom.getBalance())
    print("Abby:",abby.getBalance())