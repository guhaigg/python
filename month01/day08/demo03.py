"""
    跨函数调用
"""


# 注意：定义多个函数时,命名不能相同.
# ---------------定义函数--------------------
#               无先后顺序
def repeat_attack(count):  # 2
    list_result = []
    for i in range(count):
        result = single_attack()
        list_result.append(result)
    return list_result

def single_attack():  # 3
    print("攻击")
    return "ok"

# ---------------调用函数--------------------
state = repeat_attack(2)  # 1
print(state)  #
