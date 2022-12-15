name_list = ["张三", "李四", "王五", "王小二", "张三"]

# len 函数
print("列表中包含 %d 个元素" % len(name_list))

# count 方法
print("张山出现了 %d 次" % name_list.count("张三"))

# 从列表中删除第一次出现的数据，如果数据不存在会报错
name_list.remove("张三")
print(name_list)
