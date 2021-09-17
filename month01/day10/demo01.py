"""
    实例成员
        实例变量：表达不同个体的不同数据
            语法：对象.变量名
        实例方法：操作实例变量
            语法：
                def 方法名(self,参数):
                    方法体

                对象.方法名(数据)
"""

# [一个]全局变量,只能表达一个人的姓名,
# 不能表达不同人的姓名.
name = "双儿"
name = "建宁"



# dict01 = {"name":"双儿"}
# dict01["name"] = "双双"

class Wife:
    def __init__(self, name=""):
        # 创建实例变量
        self.name = name

    # 实例方法
    def work(self):
        print(self.name + "在工作")


shuang_er = Wife("双儿")
# 修改实例变量
shuang_er.name = "双双"
# 读取实例变量
print(shuang_er.name)
# __dict__ 存储所有实例变量
print(shuang_er.__dict__)  # {'name': '双双'}
# 通过对象访问实例方法
shuang_er.work()  # work(shuang_er)

# dict01 = {}
# dict01["name"] = "双双"
"""
# 不建议在类外创建实例变量
class Wife:
    pass


shuang_er = Wife()
# 创建实例变量
shuang_er.name = "双双"
# 读取实例变量
print(shuang_er.name)
# __dict__ 存储所有实例变量
print(shuang_er.__dict__)  # {'name': '双双'}
"""

# 不建议在__init__外创建实例变量
"""
class Wife:
    def set_name(self, name):
        # 创建实例变量
        self.name = name


shuang_er = Wife()
shuang_er.set_name("双双")
print(shuang_er.name)
print(shuang_er.__dict__)
"""
