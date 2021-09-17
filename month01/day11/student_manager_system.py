"""
    学生信息管理系统MVC
        练习:商品信息管理系统
            商品名称
            商品单价
            商品编号
            (1)输入商品信息
                V:显示菜单,选择菜单,获取信息
                C:添加信息
                M:商品模型
            (2)添加商品信息
                C:在add_commodity方法中设置cid
                  追加到列表中
            (3)显示商品信息
                V:选择菜单,打印商品列表
            (4)删除商品信息
                V:选择菜单,获取编号/显示成功或失败
                C:移除信息
            (5)修改商品信息
                V:选择菜单,获取信息/显示成功或失败
                C:修改信息
            (6)根据单价升序排列
                V:选择菜单,调用C的排序算法,显示商品
                C:排序算法
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0.0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 由系统决定的全球唯一标识符(不是用户输入的)
        self.sid = sid


class StudentView:
    """
        学生视图:输入/输出学生信息
    """

    def __init__(self):
        self.controller = StudentController()

    def display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")
        print("按5键根据成绩显示学生信息")

    def select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.input_student()
        elif item == "2":
            # 先写出调用函数代码,再快捷键生成定义函数代码
            # alt + 回车
            self.display_students()
        elif item == "3":
            self.delete_student()
        elif item == "4":
            self.set_student()
        elif item == "5":
            self.order_by_score()

    def input_student(self):
        stu = StudentModel()
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        self.controller.add_student(stu)

    def main(self):
        while True:
            self.display_menu()
            self.select_menu()

    def display_students(self):
        for item in self.controller.list_student:
            print(f"{item.name}的编号是{item.sid},年龄是{item.age},成绩是{item.score}")

    def delete_student(self):
        sid = int(input("请输入需要删除的学生编号:"))
        if self.controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

    def set_student(self):
        stu = StudentModel()
        stu.sid = input("请输入学生编号:")
        stu.name = input("请输入学生姓名:")
        stu.age = int(input("请输入学生年龄:"))
        stu.score = int(input("请输入学生成绩:"))
        if self.controller.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def order_by_score(self):
        self.controller.ascending_order()
        self.display_students()


class StudentController:
    """
        学生控制器:处理核心功能,存储...
    """

    def __init__(self):
        self.start_id = 100
        self.list_student = []

    def add_student(self, new_stu):
        # 设置学生编号(自增长)
        self.start_id += 1
        new_stu.sid = self.start_id
        # 追加到列表中
        self.list_student.append(new_stu)

    def remove_student(self, sid):
        """
            在列表中删除学生信息
        :param sid: 学生编号
        :return: 是否成功
        """
        for i in range(len(self.list_student)):
            if self.list_student[i].sid == sid:
                del self.list_student[i]
                return True  # 删除成功
        return False  # 删除失败

    def update_student(self, stu):
        """

        :param stu:
        :return:
        """
        for i in range(len(self.list_student)):
            if self.list_student[i].sid == stu.sid:
                # self.list_student[i].name = stu.name
                # self.list_student[i].age = stu.age
                # self.list_student[i].score = stu.score
                self.list_student[i].__dict__ = stu.__dict__
                return True
        return False

    def ascending_order(self):
        for r in range(len(self.list_student) - 1):
            for c in range(r + 1, len(self.list_student)):
                if self.list_student[r].score > self.list_student[c].score:
                    self.list_student[r], self.list_student[c] = self.list_student[c], self.list_student[r]


# 入口
view = StudentView()
view.main()
