from model import StudentModel


class StudentController:
    """
        学生控制器:处理核心功能,存储...
    """

    __start_id = 100  # 大家的:系统不同界面使用的学生编号是一份(连续增加)

    @classmethod
    def __set_student_id(cls, stu):
        cls.__start_id += 1
        stu.sid = cls.__start_id

    def __init__(self):
        self.__list_student = []  # 自己的:系统不同界面使用自己数据(可以显示不同数据)

    @property  # 只读属性:View类只能读取,不能修改
    def list_student(self):
        return self.__list_student

    def add_student(self, new_stu):
        # 设置学生编号
        StudentController.__set_student_id(new_stu)
        # 追加到列表中
        self.__list_student.append(new_stu)

    def remove_student(self, sid):
        """
            在列表中删除学生信息
        :param sid: 学生编号
        :return: 是否成功
        """
        stu = StudentModel(sid=sid)
        if stu in self.__list_student:
            # 重写Model类的eq方法
            self.__list_student.remove(stu)
            return True
        return False

    def update_student(self, stu):
        """

        :param stu:
        :return:
        """
        for i in range(len(self.__list_student)):
            if self.__list_student[i].sid == stu.sid:
                # self.list_student[i].name = stu.name
                # self.list_student[i].age = stu.age
                # self.list_student[i].score = stu.score
                self.__list_student[i].__dict__ = stu.__dict__
                return True
        return False

    def ascending_order(self):
        self.__list_student.sort()

# 项目部署后,应该从main.py模块执行
# 变量__name__是bll
if __name__ == "__main__":
    # 测试代码
    controller = StudentController()
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
