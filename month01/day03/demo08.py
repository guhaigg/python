"""
    真值表达式
        语法：
            if 值:  # if bool(值):
                满足条件执行的代码
        作用：
            自动判断有值,则执行if内部的代码
"""
# 值转换为bool类型的逻辑：
# 结果为False:0   0.0   ""  None
print(bool(None))

# if 4:# if bool(4):
#     print("ok")
# else:
#     print("on")

content = input("请输入内容：")
# if content != "": # 输入的不是空字符串
#     print("您输入的是" + content)
if content: # 输入的有值
    print("您输入的是" + content)

content = int(input("请输入内容："))
# if content != 0: # 输入的不是0
#     print("您输入的是" + content)
if content: # 输入的有值
    print("您输入的是" + str(content))
