gl_num = 10
gl_list = [1, 2, 3]


def demo(num, num_list):
    print("函数开始")
    num += num
    # 列表变量使用+= 不会做相加再赋值的操作，本质是在调用列表的extend方法
    # num_list.extend(num_list)
    num_list += num_list
    print(num)
    print(num_list)
    print("函数完成")


demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
