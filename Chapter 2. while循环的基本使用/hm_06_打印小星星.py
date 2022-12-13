# 在控制台连续输出5行*， 每一行星号数量依次递增

"""
row = 1

while row <= 5:
    print("*" * row)
    row += 1
"""

# 定义行的整数变量row
row = 1

# 开始循环
while row <= 5:
    col = 1 # 定义列的整数变量
    while col <= row:
        print("*", end="")
        col += 1

    print("") # 输出一行星星之后，添加换行
    row += 1

