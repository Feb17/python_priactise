gl_list = [1, 2, 3]


def demo(num_list):
    print("函数内部的代码")
    # 使用方法修改列表内容,同样会影响外部的实参
    num_list.extend([4, 5, 6])
    print(num_list)
    print("函数执行完成")


demo(gl_list)
print(gl_list)
print(num)
