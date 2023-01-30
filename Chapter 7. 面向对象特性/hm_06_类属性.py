class Tools(object):
    # 使用赋值语句定义类属性
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tools.count += 1


tool1 = Tools("斧头")
tool2 = Tools("榔头")
tool3 = Tools("水桶")

print(Tools.count)
