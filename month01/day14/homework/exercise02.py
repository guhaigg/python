"""
    2. 以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
"""


# --------------架构师--------------------
class Grenade:
    def explode(self, target):
        print("爆炸")
        # 先确定用法
        # 判断传入的对象是一种攻击目标
        if isinstance(target,AttackTarget):
            # 编码时,调用是父类
            # 运行时,执行是子类
            target.damage()

class AttackTarget:
    def damage(self):
        pass

# --------------程序员--------------------
class Player(AttackTarget):
    # 后实现功能
    def damage(self):
        print("碎屏")

class Enemy(AttackTarget):
    def damage(self):
        print("头顶爆字")

# --------------入口--------------------
grenade = Grenade()
p = Player()
grenade.explode(p)
grenade.explode(Enemy())
grenade.explode("大爷")
