"""

"""


def verify_permissions(func):
    def wrapper(*args, **kwargs):
        print("验证权限")
        return func(*args, **kwargs)

    return wrapper


@verify_permissions
def insert():
    print("插入")


@verify_permissions
def delete():
    print("删除")


insert()
delete()
