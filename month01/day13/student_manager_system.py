"""
    学生信息管理系统MVC
    练习:重构商品信息管理系统中
        --在View直接打印商品 __str__
        --在Controller通过remove移除商品 __eq__
        --在Controller通过sort排序__gt__
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0.0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid

    # 两个学生对象是否相同的依据:编号
    def __eq__(self, other):
        return self.sid == other.sid

    # 两个学生对象大小的依据:成绩
    def __gt__(self, other):
        return self.score > other.score

    # 显示学生的风格
    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},成绩是{self.score}"


class StudentView:
    """
        学生视图:输入/输出学生信息
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")
        print("按5键根据成绩显示学生信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            # 先写出调用函数代码,再快捷键生成定义函数代码
            # alt + 回车
            self.__display_students()
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__set_student()
        elif item == "5":
            self.__order_by_score()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        self.__controller.add_student(stu)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_students(self):
        for item in self.__controller.list_student:
            # print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")
            print(item)


    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号:"))
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def __set_student(self):
        stu = StudentModel()
        stu.sid = input("请输入学生编号:")
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        if self.__controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __order_by_score(self):
        self.__controller.ascending_order()
        self.__display_students()


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

# 入口
view = StudentView()
view.main()
