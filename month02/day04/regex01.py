"""
正则表达式元字符学习
"""
import re

# 普通字符匹配自身
# result = re.findall("ab","abcdabcda")
# print(result)

# 或关系
# result = re.findall("ab|bc","abcdbcda")
# print(result)

# 匹配任意一个字符
# result = re.findall('张.丰',"张三丰,张四丰,张五丰")
# print(result)

# 匹配字符集  & 反集
# result = re.findall('[ !A-Z]',"How are you!")
# print(result)
#
# result = re.findall('[^ !A-Z]',"How are you!")
# print(result)

# 匹配重复
# 0次到多次
# result = re.findall('wo*',"wooooo~~w!")
# print(result)

# 1次到多次
# result = re.findall('wo+',"wooooo~~w!")
# print(result)

# 0次或1次
# result = re.findall('wo?',"wooooo~~w!")
# print(result)

# 一定的次数区间
# result = re.findall('wo{3}',"wooooo~~w!")
# print(result)
# result = re.findall('wo{2,4}',"wooooo~~w!")
# print(result)


# 匹配开头结尾位置
# result = re.findall('^Jame',"Jame,hello")
# print(result)
#
# result = re.findall('Jame$',"hi,Jame")
# print(result)


# 匹配数字
# result = re.findall('\d{1,5}',"Mysql: 3306, http:80")
# print(result)
#
# result = re.findall('\D+',"Mysql: 3306, http:80")
# print(result)

# 匹配普通字符
# result = re.findall('\w+',"server_port = 8888")
# print(result)
#
# result = re.findall('\W+',"server_port = 8888")
# print(result)

# 匹配空字符 和非空字符
# result = re.findall('\w+\s+\w+',"hello    world")
# print(result)
#
# result = re.findall('\S+',"C119-lei&3 sddf daf")
# print(result)

# 单词边界位置
# result = re.findall(r'\bis',"This is a test.")
# print(result)

# 匹配特殊符号
# result = re.findall("\d+\.?\d*","3.14 78 0.618 5.12 20")
# print(result)

# 贪婪 --》 非贪婪
# result = re.findall("a\w+c","abbbbcbbbbbc")
# print(result)
# result = re.findall("a\w+?c","abbbbcbbbbbc")
# print(result)

# 子组
# data = "张三：1996，李四：1998，王五：1997"
# result = re.findall("(张三)：(\d+)",data)
# print(result)


result = re.search("(ab)+","ababababab")
print(result.group()) # group取值

result = re.search("(?P<xing>王|李)\w{1,3}","王者荣耀")
print(result.group()) # group取值




