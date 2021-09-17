"""
    可迭代对象工具箱
        为什么自定义IterableHelper类?
            1. 教学角度:学习函数式编程思想(分隔做),
                并非只学习内置高阶函数.
            2. 面试角度:精通函数式编程
                    参照微软Linq技术的思想,创建了自定义集成操作框架
            3. 实用角度:功能强大到无限
        备注:不如内置高阶函数性能高

"""


class IterableHelper:
    """
        (集成操作框架)
        可迭代对象助手类:封装对可迭代对象操作的常用高阶函数
    """

    @staticmethod
    def find_all(iterable, condition):
        """
            在可迭代对象中,根据任意条件查找所有元素
        :param iterable:可迭代对象
        :param condition:函数类型,搜索条件
        :return:生成器对象,推算满足条件的元素
        """
        for number in iterable:
            if condition(number):
                yield number

    @staticmethod
    def find_single(iterable, condition):
        """
            在可迭代对象中,根据任意条件查找单个元素
        :param iterable:可迭代对象
        :param condition:函数类型,搜索条件
        :return:满足条件的元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def get_count(iterable, condition):
        """
            在可迭代对象中,根据任意条件计算数量
        :param iterable:可迭代对象
        :param condition:函数类型,搜索条件
        :return:int类型,满足条件的数量
        """
        count = 0
        for item in iterable:
            if condition(item):
                count += 1
        return count

    @staticmethod
    def select(iterable, condition):
        """
            在可迭代对象中,根据处理逻辑选择元素的属性
        :param iterable:可迭代对象
        :param condition:函数类型,对每个元素的处理逻辑
        :return:生成器,推算元素的属性
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def delete_all(iterable, condition):
        """
            根据条件删除可迭代对象中所有元素
        :param iterable:可迭代对象
        :param condition:函数类型,删除条件
        :return:int类型,删除数量
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def delete_single(iterable, condition):
        """
            根据条件删除可迭代对象中单个元素
        :param iterable:可迭代对象
        :param condition:函数类型,删除条件
        :return:bool类型,是否删除成功
        """
        for i in range(len(iterable)):
            if condition(iterable[i]):
                del iterable[i]
                return True
        return False

    @staticmethod
    def get_max(iterable, condition):
        """
            根据条件在可迭代对象中获取最大元素
        :param iterable: 可迭代对象
        :param condition: 函数类型,查找条件
        :return: 最大元素
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def get_min(iterable, condition):
        """
           在可迭代对象中,根据条件查找最小元素
           :param iterable:可迭代对象
           :param condition:函数类型的参数
           :return:最小元素
        """
        min_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(min_value) > condition(iterable[i]):
                min_value = iterable[i]
        return min_value

    @staticmethod
    def order_by(iterable, condition):
        """
            根据条件对可迭代对象进行升序排列
        :param iterable:可迭代对象
        :param condition:函数类型,搜索条件
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) > condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def descending_order(iterable, condition):
        """
           根据条件对可迭代对象降序排列
           :param iterable:可迭代对象
           :param condition:函数类型的参数
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) < condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
