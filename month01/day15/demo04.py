"""
    小结 - 程序结构
    1. 项目根目录
        包
            模块
                类
                    方法
        main.py

    2. 相关概念
        根目录:主模块所在文件夹
        主模块:第一次执行的模块,不会生成pyc文件.

    3. 导入模块
        import 模块
        模块.成员

        import 包.模块 as 别名
        别名.成员

        from 模块 import 成员
        直接访问成员

        from 模块 import *
        直接访问成员

    4. 导入包
        备注:必须在包的__init__.py模块中提供成员

        import 包
        模块.成员

        import 包.包 as 别名
        别名.成员

        from 包 import 成员
        直接访问成员

        from 包 import *
        直接访问成员

    5. 导入模块是否成功的唯一标准
        导入路径 + 系统路径 = 真实路径
"""
import sys

print(sys.path)