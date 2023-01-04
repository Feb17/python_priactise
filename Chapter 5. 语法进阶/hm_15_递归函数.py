def demo(num):
    print(num)
    # 递归函数必须设置出口，否则死循环
    if num == 1:
        return
    # 函数自己调用自己
    demo(num - 1)


demo(3)
