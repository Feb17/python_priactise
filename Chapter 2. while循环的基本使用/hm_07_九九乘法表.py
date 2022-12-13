# 定义行的整数变量row
row = 1

# 开始循环
while row <= 9:
    col = 1  # 定义列的整数变量
    while col <= row:
        result = col * row  # 定义变量存储乘法运算结果
        print("%d * %d = %d" % (col, row, result), end="\t")  # \t 在控制台输出一个 制表符， 协助在输出文本的时候 垂直方向保持对齐
        col += 1

    print("")  # 输出一行之后，添加换行
    row += 1
