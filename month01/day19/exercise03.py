"""
    为sum_data,增加打印函数执行时间的功能.
"""
import time


def print_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        data = func(*args, **kwargs)
        stop = time.time()
        print("执行时间是：", stop - start)
        return data

    return wrapper


@print_execution_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
