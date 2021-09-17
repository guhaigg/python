"""
基于 inet.log完成
编写程序，通过输入一个接口名称（每段首个单词）
打印出这个接口描述信息中的address is 的值

提示： 段落之间有空行
      接口名称是每段第一个单词

思路： 根据输入的接口名称找到段落
      在段落中匹配目标
"""
import re


# 　生成器　－－》　每次得到一段内容
def get_parg():
    file = open("inet.log")
    # 每次循环获取一段内容
    while True:
        data = ''
        for line in file:
            if line == "\n":
                break  # 遇到空行
            data += line
        if data:
            yield data  # 提供一段内容
        else:
            file.close()
            return


def main():
    port = input("输入接口名称：")
    # 　每次得到一段内容，验证这一段是否为想要的
    for info in get_parg():
        # 　匹配一段首个单词
        head = re.match("\S+", info).group()
        # 如果是需要的段落匹配目标内容
        if head == port:
            result = re.search("([0-9a-f]{4}\.?){3}", info)
            if result:
                return result.group()
            else:
                return "Unknown"


if __name__ == '__main__':
    print("找到的地址:",main())
