"""
    玩家攻击敌人,敌人受伤,还可能死亡(加分)
          (头顶爆字,扣除血量)

    敌人攻击玩家,玩家受伤,还可能死亡(游戏结束)
          (闪现红屏,扣除血量)
"""


class Character:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    # 子类完全相同
    def attack(self, target):
        print("发起攻击")
        target.damage(self.atk)

    # 子类部分相同
    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.death()

    # 子类完全不同
    def death(self):
        pass

class Player(Character):
    def damage(self, value):
        print("闪现红屏")
        super().damage(value)

    def death(self):
        print("游戏结束")

class Enemy(Character):
    def damage(self, value):
        print("头顶爆字")
        super().damage(value)

    def death(self):
        print("加分")

p = Player(100, 25)
e = Enemy(50, 10)
p.attack(e)
e.attack(p)
p.attack(e)
