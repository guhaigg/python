"""
    汇率转换器
    创建文件:exercise01
"""
# 1. 获取数据：xxx美元
usd = float(input("请输入美元:"))
# 2. 逻辑计算：yyy人民币= xxx美元×6.4609
cny = usd * 6.4609
# 3. 显示结果：xxx美元=yyy人民币
print(str(usd) + "美元=" + str(cny) + "人民币")
