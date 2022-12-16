hello_str = "hello world"

# 1. 判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2. 判断是否以指定字符结尾
print(hello_str.endswith("world"))

# 3. 查找指定字符串
print(hello_str.find("llo"))
print(hello_str.find("abc"))
# find 如果指定的字符串不存在，会返回-1
# index 如果指定的字符串不存在，会报错
print(hello_str.index("llo"))
# print(hello_str.index("abc"))

# 4. 替换指定字符串
# replace方法执行完成后，会返回一个新的字符串
# 不会修改原来的字符串的内容
print(hello_str.replace("world", "python"))
print(hello_str)
