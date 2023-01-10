class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count
        print("已装填[%d发]子弹" % count)

    def shoot(self):
        if self.bullet_count <= 0:
            return "[%s]没有子弹了..." % self.model

        self.bullet_count -= 1
        print("[%s] 突突突 [剩余子弹：%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            return "%s没有枪，无法射击" % self.name

        # 2. 喊口号
        print("冲啊")

        # 3. 让枪装填子弹
        # Ak47.add_bullet(50)
        self.gun.add_bullet(50)

        # 4. 让枪发射子弹
        self.gun.shoot()


# 1. 创建枪对象
Ak47 = Gun("AK47")

# 2. 创建士兵对象
XuSanDuo = Soldier("许三多")
XuSanDuo.gun = Ak47
XuSanDuo.fire()
