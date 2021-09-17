"""

"""

# 导入方式1:导入文件
# 适用性:面向过程的技术(全局变量/函数)
import module_exercise

print(module_exercise.data)
module_exercise.func01()
# 通过对象访问实例方法
m = module_exercise.MyClass()
m.func02()
module_exercise.MyClass.func03()

# 导入方式2:导入文件中的成员
# 适用性:面向对象的技术(类)
from module_exercise import *

print(data)
func01()
m = MyClass()
m.func02()
MyClass.func03()
