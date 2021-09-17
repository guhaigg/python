"""
    str 字面值
"""
# 双引号
data01 = "悟空"
# 单引号
data02 = '悟空'
# 三引号：可见即所得
data03 = '''悟空'''
data04 = """
悟
    空
"""
print(data04)

# 引号冲突
name = '花果山"水帘洞"齐天大圣孙悟空'
name = "花果山'水帘洞'齐天大圣孙悟空"
name = """花果山'水帘洞'齐天"大圣"孙悟空"""

# 转义字符:改变字符的原始含义
# \"   \'   \\   Tab键\t   换行\n
name = "花果山水帘洞齐天\"大圣\"孙悟空"
url = "C:\\arogram Files\\bnternet Explorer\cmages"
url = r"C:\arogram Files\bnternet Explorer\cmages"
name = "孙\t悟\n空"
print(name)