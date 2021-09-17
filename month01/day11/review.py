"""
    复习－跨类调用
    1. 为什么创建类?
        有多个数据需要包装
        有行为需要承担
    2. 为什么创建多个类?
        根据变化点,分担多个职责.
    3. 划分职责的原则:
        行为不同用类区分,数据不同用对象区分
            老张类     开车类
           驾驶方法   行驶方法

           张无忌对象    赵敏对象
                 教
    4.　语法
    --1. 直接创建对象
    class A:
        def　func01():
            b = B()
            b.func02()

    class B:
        def　func02():
            pass

    --2.  在构造函数中创建对象
    class A:
        def __init__():
            self.b = B()

        def　func01():
            self.b.func02()

    class B:
        def　func02():
            pass

    --3. 通过参数传递对象
    class A:
        def　func01(c):
            c.func02()

    class B:
        def　func02():
            pass

    a = A()
    a.func01(  B()  )
"""
