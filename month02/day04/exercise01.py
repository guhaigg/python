"""
正则表达式元字符练习
"""
import re

# 从字符串中匹配出大写字母开头单词 How are you Jame!
# result = re.findall("[A-Z][a-z]*","I am Jame!")
# print(result)

# 从字符串中匹配出所有数字 2021-8-31
# result = re.findall("\d+","2021-8-31")
# print(result)

# 从字符串中匹配出所有数字
# result = re.findall("-?\d+","18岁小战士在-15度天气中负重20Kg")
# print(result)

# 匹配一下 手机号码和qq号码
# result = re.findall(r"\b1[3-9]\d{9}\b","王总:13845683568,卡号:69781584999658936")
# print(result)
# result = re.findall("[1-9]\d{5,9}","马总：5188888")
# print(result)


# 验证这个用户名是否为 6-12位数字字母下划线构成
# user = input("User:")
# if re.findall("^[_0-9a-zA-Z]{6,12}$",user):
#     print(True)
# else:
#     print(False)

# 匹配薪资
# result = re.findall("\$\d+","日薪: $150")
# print(result)

# 匹配书名
# books="《葫芦娃——@妖精》,《奥特曼 ～～ 小怪兽》,《哈利波特 之 2021》"
# result = re.findall("《.+?》",books)
# print(result)

# 匹配IP地址 192.168.4.56
result = re.search("(\d{1,3}\.?){4}","IP地址: 192.168.4.56")
print(result.group())




