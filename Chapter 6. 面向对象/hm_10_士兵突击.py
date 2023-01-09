class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            return "[%s]没有子弹了..." % self.model

        self.bullet_count -= 1
        print("[%s] 突突突 [剩余子弹：%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None


# 1. 创建枪对象
ak47 = Gun("AK47")

ak47.add_bullet(50)
ak47.shoot()
