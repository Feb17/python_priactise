for num in [1, 2, 3]:

    print(num)
    if num == 2:
        break
else:
    # 如果循环体内部使用break，else下方的代码则不会被执行
    print("会执行吗")
print("循环结束")
