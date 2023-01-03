def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wet = 50
    print("测量结束...")

    # 元组 - 可以包含多个数据
    # 如果函数返回的类型是元组，小括号可以省略
    # return (temp, wet)
    return temp, wet


result = measure()
print(result)

# 需要单独的处理温度或者湿度
print(result[0])
print(result[1])

# 如果函数返回的类型是元组，同时希望单独的处理元组中的数据
# 可以使用多个变量，接收函数返回的结果
# 注意：使用多个变量接收结果是，变量的个数应该和元组中的元素个数保持一致
gl_temp, gl_wet = measure()
print(gl_temp)
print(gl_wet)
