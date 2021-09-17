"""
    练习2:
    在终端中输入性别
    打印"您好先生" "您好女士" "未知"
"""

sex = input("请输入性别：")
if sex == "男":
    print("您好先生")
elif sex == "女":
    print("您好女士")
else:
    print("未知")
