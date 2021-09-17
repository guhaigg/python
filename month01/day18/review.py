"""
    函数式编程
        函数作为参数
            适用性:多个函数,主体部分相同,核心算法不同
                def 功能1():
                    相同代码
                    不同代码1

                def 功能2():
                    相同代码
                    不同代码2

            思想:分--将不同代码单独定义到函数中
                隔--将变化点抽象为参数
                    通过参数调用传入的变化函数
                    隔离通用功能与不同代码之间的变化
                做--
                def 变化点1():
                    不同代码1

                def 变化点2():
                    不同代码2

                def 通用功能(变化点):
                    相同代码
                    # 变化点1()
                    # 变化点2()
                    # 变化点xxx()
                    变化点()

                通用函数( 变化点1  )
                通用函数( 变化点2  )

                def 变化点3():
                    不同代码3

                通用函数( 变化点3  )

        函数作为返回值
"""