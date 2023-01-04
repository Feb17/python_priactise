def demo(num):
    # 出口
    if num == 0:
        return 0
    # 数字累加
    temp = demo(num - 1)
    return num + temp


result = demo(100)
print(result)
