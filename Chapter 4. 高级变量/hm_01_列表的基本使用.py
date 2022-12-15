name_list = ["A", "B", "C"]
name_list2 = ["a", "b", "c", "d"]
# 1. 取值和取索引
print(name_list[0])
print(name_list.index("A"))

# 2. 修改
name_list[1] = "李四"
print(name_list)

# 3. 增加
name_list.append("D")
print(name_list)

name_list.insert(0, "张三")
print(name_list)

name_list.extend(name_list2)
print(name_list)

# 4. 删除
name_list.remove("A")
print(name_list)

# 默认删除列表最后一个元素
name_list.pop()
print(name_list)

# 指定删除索引位置的元素
name_list.pop(6)
print(name_list)

name_list.clear()
print(name_list)

# del 将变量从内存中删除
del name_list2[0]
print(name_list2)
