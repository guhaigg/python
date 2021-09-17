"""
    以面向对象思想,描述下列情景.
        练习:
        玩家(攻击力)攻击敌人(血量),
        敌人受伤(减血,头顶爆字,还有可能死亡[掉金币]).

        敌人(攻击力)攻击玩家(血量),
        玩家受伤(减血,碎屏,还有可能死亡[游戏结束]).
"""


class Player:
    def __init__(self, hp=0, atk=0):
        self.atk = atk
        self.hp = hp

    def attack(self, target):
        print("发起攻击")
        target.damage(self.atk)

    def damage(self, value):
        print("碎屏")
        self.hp -= value
        if self.hp <= 0:
            self.death()

    def death(self):
        print("游戏结束")


class Enemy:
    def __init__(self, hp=0, atk=0):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        self.hp -= value
        print("头顶爆字")
        if self.hp <= 0:
            self.death()

    def death(self):
        print("掉金币")

    def attack(self, target):
        print("发起攻击")
        target.damage(self.atk)


p = Player(500, 50)
e = Enemy(100, 20)
# 玩家打一次敌人
p.attack(e)
# 敌人打一次玩家
e.attack(p)
print("玩家血量:", p.hp)
print("敌人血量:", e.hp)
