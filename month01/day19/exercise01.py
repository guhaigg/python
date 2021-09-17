"""

"""
def verify_permissions(func):
    def wrapper():
        print("验证权限")
        func()

    return wrapper


def insert():
    print("插入")


def delete():
    print("删除")


insert = verify_permissions(insert)
delete = verify_permissions(delete)

insert()
delete()
