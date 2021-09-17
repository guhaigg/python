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

