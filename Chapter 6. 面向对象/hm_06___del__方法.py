class Cat:
    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 走了" % self.name)


# tom 是一个全局变量
tom = Cat("汤姆")

# del 关键字可以删除一个 对象
del tom

print("-" * 50)
