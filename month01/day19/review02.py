# 二：
#     类型标注
# 为变量增加类型
from typing import List


class D:
    def __init__(self):
        self.list_data =[ ] # type:List[str]
    def add(self, data):
        self.list_data.append(data)

    def removeed(self)->list:
        pass

controller =D()
controller.add('EW')
controller.add('VASV')
# controller.add(True)
for item in controller.list_data:
    print(item.lower())
result = controller.removeed()
result.append('dw')
