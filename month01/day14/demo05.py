"""

"""

# "我过去"
# 语法:import 模块名
# 使用:模块名.成员
# 本质:创建文件,关联目标模块地址
import module01

module01.func01()
module01.func02()

# "你过来"
# 语法:from 模块名 import 成员
#      直接使用成员
# 本质:将目标模块中的成员导入到当前模块作用域中
# 注意:小心命名冲突
# from module01 import func01
# from module01 import func01,func02
from module01 import *

def func01():
    print("dmoe05-func01")

func01()
