"""
    字典推导式
        根据可迭代对象,简单的创建新字典
        字典名 = {键 : 值 for 变量 in 可迭代对象}
        字典名 = {键 : 值 for 变量 in 可迭代对象 if 条件}

"""
# dict_numbers = {}
# for number in range(1,11):
#     dict_numbers[ number ] =  number + 10
# print(dict_numbers)
dict_numbers = {number: number + 10 for number in range(1, 11)}
dict_numbers = {number: number + 10 for number in range(1, 11) if number % 2 == 0}
print(dict_numbers)

