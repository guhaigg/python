"""
    数据模型
"""
from typing import Optional


class HouseModel:
    """
        房源模型
    """

    def __init__(self, id: Optional[int] = 0, title: Optional[str] = "",
                 community: Optional[str] = "", years: Optional[str] = "",
                 house_type: Optional[str] = "", area: Optional[int] = 0.0,
                 floor: Optional[str] = "", description: Optional[str] = "",
                 total_price: Optional[float] = 0.0,
                 unit_price: Optional[float] = 0.0,
                 follow_info: Optional[str] = ""):
        """
            创建房源信息对象
        :param id:编号
        :param title: 标题
        :param community: 小区
        :param years:年份
        :param house_type:房型
        :param area:建筑面积
        :param floor:底层
        :param description:描述信息
        :param total_price:总价
        :param unit_price:单价
        :param follow_info:带看记录
        """
        self.id = id  # type:float
        self.title = title  # type:str
        self.community = community  # type:str
        self.years = years  # type:str
        self.house_type = house_type  # type:str
        self.area = area  # type:float
        self.floor = floor  # type:str
        self.description = description  # type:str
        self.total_price = total_price  # type:float
        self.unit_price = unit_price  # type:float
        self.follow_info = follow_info  # type:str

    def __str__(self):
        # 偷懒了
        # return str(self.__dict__)
        return (f'编号是{self.id}标题是{self.title}小区是{self.community}年份是{self.years}\
                房型是{self.house_type}建筑面积{self.area}底层{self.floor}描述信息{self.description}\
                总价{self.total_price}单价{self.unit_price}带看记录{self.follow_info}')


def __gt__(self, other):
    return self.total_price > other.total_price
