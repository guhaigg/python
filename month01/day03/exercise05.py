"""
    在终端中录入4个同学身高,打印最高的值.
    算法：
    170  160  180  165
    假设第一个就是最大值
    使用假设的和第二个进行比较, 发现更大的就替换假设的
    使用假设的和第三个进行比较, 发现更大的就替换假设的
    使用假设的和第四个进行比较, 发现更大的就替换假设的
    最后，假设的就是最大的.
"""
height01 = int(input("请输入身高:"))
height02 = int(input("请输入身高:"))
height03 = int(input("请输入身高:"))
height04 = int(input("请输入身高:"))
max_value = height01
if max_value < height02:
    max_value = height02
if max_value < height03:
    max_value = height03
if max_value < height04:
    max_value = height04
print("最大值是:"+str(max_value))