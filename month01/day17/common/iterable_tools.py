"""
    可迭代对象工具箱
"""
class IterableHelper:
    """
        可迭代对象助手类:封装对可迭代对象操作的常用高阶函数
    """

    @staticmethod
    def find_all(iterable,condition):
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
    def find_single(iterable,condition):
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
    def get_count(iterable,condition):
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
    def select(iterable,condition):
        """
            在可迭代对象中,根据处理逻辑选择元素的属性
        :param iterable:可迭代对象
        :param condition:函数类型,对每个元素的处理逻辑
        :return:生成器,推算元素的属性
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def delete_all(iterable,condition):
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