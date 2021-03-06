"""
    小结-面向对象
    一. 语法
        class 类名:
            类变量 = 数据

            @classmethod
            def 类方法(cls):
                 通过 cls.类变量 操作类变量

            def __init__(self,参数):
                self.实例变量 = 参数

            def 实例方法(self):
                通过 self.实例变量 操作数据

        对象 = 类名(数据)
        对象.实例变量
        对象.实例方法()

        类名.类变量
        类名.类方法()


    二. 设计思想
        封装:根据需求划分为多个类
        继承:统一多个变化类型,隔离客户端代码与多个变化类型
        多态:多个变化类型通过重写实现具体功能
        目标:满足开闭原则
                允许增加新功能,但是不修改客户端代码
"""