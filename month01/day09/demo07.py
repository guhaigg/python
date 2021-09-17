"""
    面向对象思考流程：
      现实世界             软件世界
      客观事物              app(滴滴打车)
       汽车 --抽象化--> 类 --具体化--> 对象
                     品牌            奔驰
                     车牌            007
                     颜色            白色
                           ...
"""

# 类
class Wife:
    # 数据
    def __init__(self, name, age=20, face_score=60):
        self.name = name
        self.age = age
        self.face_score = face_score

    # 行为-方法(函数)
    def work(self):
        print(self.name + "在工作")


# 实例化
# 创建对象(自动调用__init__)
shuang_er = Wife("双儿", 23, 93)
# 读取对象数据
print(shuang_er.name)
# 调用对象方法
shuang_er.work() # work(shuang_er)

jian_ning = Wife("建宁")
# 修改对象数据
jian_ning.face_score = 95
jian_ning.work()