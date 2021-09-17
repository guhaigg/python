"""
    面向对象三大特征:
        封装:根据需求划分为多个类    [分]
            例如:创建Person/Car/Airplane类
        继承:将多个变化的类型抽象为一个概念   [隔]
                例如:创建父类Vehicle
            将多个变化类型的行为统一
                例如:统一Car/Airplane类型的transport方法
            隔离客户端代码,与多个变化类型
                例如:隔离Person与Car/Airplane
        多态:对于父类同一行为,在不同的子类中有不同的实现
                例如:对于Vehicle的transport方法,在Car/Airplane类中有不同实现
            多个变化类型通过重写实现具体功能   [做]
                例如:Car/Airplane重写transport方法的内容
"""