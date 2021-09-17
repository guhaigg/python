from usl import EmployeeView

if __name__ == '__main__':
    # 只有当前模块为主模块,才执行入口逻辑.
    view = EmployeeView()
    view.main()