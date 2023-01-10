class Women:
    def __init__(self, name):
        self.name = name

        # 私有属性__age
        self.__age = 18

    # 私有方法__secret
    def __secret(self):
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Women("小芳")

# 无法在外界直接调用私有属性和私有方法
# print(xiaofang.__age)
# xiaofang.__secret()

print(xiaofang._Women__age)
xiaofang._Women__secret()
