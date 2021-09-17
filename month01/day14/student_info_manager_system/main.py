from usl import StudentView

# 如果是主模块才执行
# 快捷键:main+回车
if __name__ == '__main__':
    # (被导入时不执行)
    view = StudentView()
    view.main()
