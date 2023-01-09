class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f 平方" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f [剩余面积：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 %s" % item)

        # 1. 判断家具的面积
        if self.free_area <= item.area:
            print("放不下了")
            return

        # 2. 将家具的名称添加到列表
        self.item_list.append(item.name)

        # 3. 剩余面积减去添加家具的面积
        self.free_area -= item.area


# 1. 创建家具对象
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)

# 2. 创建房子对象
myhome = House("两室一厅", 60)

myhome.add_item(bed)
myhome.add_item(chest)
myhome.add_item(table)
print(myhome)
