class Cat:

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建对象
tom = Cat()

# 创建属性
tom.name = "汤姆"

tom.eat()
tom.drink()

# 再创建一个猫对象
lazy_cat = Cat()

# 创建属性
lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()
