class Cat:
    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)

    def __str__(self):
        # __str__必须返回字符串
        return "我是小猫[%s]" % self.name


tom = Cat("汤姆")
print(tom)
