class Cat:

    def __init__(self):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = "汤姆"

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 创建对象时，会自动调用__init__方法。不需要tom.__init__()来手动调用
tom = Cat()
# tom.__init__()
print(tom.name)
tom.eat()
