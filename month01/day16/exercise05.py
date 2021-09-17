"""
    练习1：定义函数,在列表中找出所有偶数
     [43,43,54,56,76,87,98]

    练习2：定义函数,在列表中找出所有数字
     [43,"悟空",True,56,"八戒",87.5,98]
"""
# 练习1：
list01 = [43, 43, 54, 56, 76, 87, 98]


def find_all_even():
    for item in list01:
        if item % 2 == 0:
            yield item


result = find_all_even()
for number in result:
    print(number)

# 练习2：
list02 = [43, "悟空", True, 56, "八戒", 87.5, 98]


def find_all_number():
    for item in list02:
        # if type(item) == int or type(item) == float:
        if type(item) in (int, float):
            yield item


for number in find_all_number():
    print(number)
