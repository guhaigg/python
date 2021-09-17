"""
    在终端中录入4个同学体重,打印最轻的值.
	效果：
        请输入第1个同学体重:100
        请输入第2个同学体重:120
        请输入第3个同学体重:93
        请输入第4个同学体重:160
        最轻的同学:93
"""
weight01 = int(input("请输入第1个同学体重:"))
weight02 = int(input("请输入第2个同学体重:"))
weight03 = int(input("请输入第3个同学体重:"))
weight04 = int(input("请输入第4个同学体重:")) 

min_value = weight01
if min_value > weight02:
    min_value = weight02
if min_value > weight03:
    min_value = weight03
if min_value > weight04:
    min_value = weight04

print("最轻的同学：" + str(min_value))
