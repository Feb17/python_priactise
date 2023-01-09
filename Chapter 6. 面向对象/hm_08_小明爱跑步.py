class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s，体重是%.2f 公斤" % (self.name, self.weight)

    def run(self):
        self.weight = self.weight - 0.5

    def eat(self):
        self.weight = self.weight + 1


XiaoMing = Person("小明", 75)
XiaoMei = Person("小美", 45)
XiaoMing.run()
XiaoMing.eat()

XiaoMei.run()
XiaoMei.eat()

print(XiaoMing)

print(XiaoMei)
