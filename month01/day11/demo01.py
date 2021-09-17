"""
    在玩家攻击敌人时,传递数据
    以面向对象思想,描述下列情景.
        玩家(攻击力)攻击敌人(血量),
        敌人受伤(减血,头顶爆字,还有可能死亡).

"""
"""
class Player:
    def attack(self,target): # 2
        print("发起攻击")
        target.damage()

class Enemy:
    def damage(self): # 3         #  ?
        print("头顶爆字")

p = Player()
e = Enemy()
# 由使用决定Player调用Enemy
p.attack(e)# 1
"""

"""
class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, target):
        print("发起攻击")
        target.damage(self) # 将玩家传入到敌人类中


class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, other):
        self.hp -= other.atk# 敌人因为玩家攻击力而减血
        print("头顶爆字")
        if self.hp <= 0:
            self.death()

    def death(self):
        print("掉金币")


p = Player(50)
e = Enemy(100)
p.attack(e)
p.attack(e)
"""


class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def attack(self, target):
        print("发起攻击")
        target.damage(self.atk)

class Enemy:
    def __init__(self, hp=0):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("头顶爆字")
        if self.hp <= 0:
            self.death()

    def death(self):
        print("掉金币")


p = Player(50)
e = Enemy(100)
p.attack(e)
p.attack(e)