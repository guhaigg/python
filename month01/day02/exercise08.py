"""
    练习2：古代的秤，一斤十六两。
    在终端中获取两，计算几斤零几两。
"""
total_liang = int(input("请输入总两数："))
jin = total_liang // 16
liang = total_liang % 16
print("结果为："+str(jin)+"斤"+str(liang)+"两")