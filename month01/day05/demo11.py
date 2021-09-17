"""
   字符串 -> 列表
"""
# 使用一个字符串存储多个信息
list_result = "唐僧,孙悟空,八戒".split(",")
print(list_result)  # ['唐僧', '孙悟空', '八戒']

str_data_time = input("请输入日期yyyy/mm/dd：")
list_data_time = str_data_time.split("/")
print(list_data_time)
