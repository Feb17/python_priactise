class Tools(object):
    # 创建类属性
    count = 0

    # 创建类方法
    @classmethod
    def show_tools_count(cls):
        print("工具对象的数量 %d" % cls.count)

    # 创建对象方法
    def __init__(self, name):
        # 定义对象属性self.name 传入形参name
        self.name = name
        Tools.count += 1


tool1 = Tools("斧头")
tool2 = Tools("榔头")
tool3 = Tools("水桶")

Tools.show_tools_count()
