class Cat:
    # 初始化方法，用于设置对象的属性和属性的初始值
    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        # self.name = "汤姆"
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 创建对象时，会自动调用__init__方法。不需要tom.__init__()来手动调用
tom = Cat("汤姆")
# tom.__init__()
tom.eat()

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
