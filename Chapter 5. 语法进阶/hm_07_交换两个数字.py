a = 6
b = 100

# 解法1
# c = a
# a = b
# b = c


# 解法2
# a = a + b
# b = a - b
# a = a - b

# 解法3
# a, b = (b, a)
# 等号右边是元组，省略了小括号
a, b = b, a
print(a, b)
