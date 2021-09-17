"""
    逻辑运算符
        判断两个命题关系
            并且：命题  and  命题
                两个都得满足

            或者：命题  or  命题
                满足一个就行

            not  命题
"""
# 来自于丈母娘的灵魂质问：
# 有钱  and  有房
# print(float(input("请输入存款：")) > 1000000 and input("请输入是否有房：") == "有")

# 有钱  or  有房
print(float(input("请输入存款：")) > 1000000 or input("请输入是否有房：") == "有")

# not
print(not True) # False