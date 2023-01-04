def demo(*args):
    num = 0
    for n in args:
        num += n
    return num


print(demo(1, 2, 3, 4))
