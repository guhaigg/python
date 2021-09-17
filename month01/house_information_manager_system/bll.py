"""
    业务逻辑层
""" 
from dal import HouseDao
from common import iterable_tools

class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()
        self.__list_type =[]

    @property
    def list_houses(self):
        """
            所有房源信息
        """
        return self.__list_houses
    def price_max(self):
        # return max(self.__list_houses)
        return max(self.__list_houses,key=lambda house :house.total_price )
    def area_min(self):
        return min(self.__list_houses, key=lambda house: house.area)
    def total(self,item):
        return item.total_price

    def order_by(self):
        # iterable_tools.IterableHelper.order_by(self.__list_houses,self.total)


        return sorted(self.__list_houses,key=lambda house: house.total_price)

    def get_type(self):
        for i in map(lambda house: house.house_type,self.__list_houses):
            self.__list_type.append(i)
        b = list(set(self.__list_type))
        for i in b:
            z = 0
            for x in self.__list_type:
                if x == i:
                    z +=1
            print(f'{i}户型有{z}栋',end='')





