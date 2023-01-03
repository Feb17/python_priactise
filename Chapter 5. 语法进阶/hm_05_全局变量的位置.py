# 在开发时，应该把模块中的所有全局变量定义在所有函数上方

num = 10


def demo():
    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


# 再定义一个全局变量
title = "程序员"

demo()

# 再定义一个全局变量
name = "小明"
