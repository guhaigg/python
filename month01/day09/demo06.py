"""
    函数参数
        形式参数：限制实参
            1.位置形参:实参必填
                    def 函数名(参数1,参数2)
            2.默认形参:实参可选
                    def 函数名(参数1=数据,参数2=数据)
            3.星号元组形参:位置实参数量无限　
                    def 函数名(*参数)
            4.双星号字典形参:关键字实参数量无限　
                    def 函数名(**参数)
            5.命名关键字形参：必须关键字实参
                    def 函数名(*参数1,参数2)
                    def 函数名(*,参数2)

        实际参数:与形参进行对应
            6.位置实参:按顺序
                    函数名(数据1,数据2)
                8.序列实参:拆,用元素
                    函数名(*序列)
            7.关键字实参:按名字
                    函数名(参数1=数据,参数2=数据)
                9.字典实参:拆,用键值对
                        函数名(**字典)
"""
# 实践:
message = "我爱Python编程"
# 判断字符串是否以某个字符开头
print(message.startswith("我"))  # True
print(message.startswith("爱"))  # False
print(message.startswith("我爱"))  # True
print(message.startswith("我爱y"))  # False
# 限制搜索范围
print(message.startswith("Python",2))  # False
print(message.startswith("Py",2,-2))  # False

# 在字符串中查找某个字符的正向索引,如果不存在则返回-1
print(message.find("Python")) # 2
