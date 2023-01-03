def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))


# 1. 定义一个数字的变量
a = [1, 2, 3]

print("a变量保存数据的内存地址是 %d" % id(a))
