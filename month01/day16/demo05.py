"""
    yield --> 生成器函数
"""

"""
class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        number = 0
        while number <  self.__stop:
            yield number
            number += 1



# for number in MyRange(5):
#     print(number)# 0 1 2 3 4

# 循环一次  计算一次  返回一次
# 每次都存储当前结果,释放之前结果
m_range = MyRange(8)
iterator = m_range.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
"""

"""
# 生成器的伪代码
class generator:# 生成器对象 = 
    def __iter__(self):# 可迭代对象
        return self
    
    def __next__(self):# 迭代器对象
        产生数据 
"""


def my_range(stop):
    number = 0
    while number <  stop:
        yield number
        number += 1


# print(my_range(5))

for item in my_range(5):
    print(item)

# result = my_range(9999999999999999999999999999999)
# iterator = result.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except StopIteration:
#         break