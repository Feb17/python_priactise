def demo1():
    return int(input('Enter a number: '))


def demo2():
    return demo1()


try:
    print(demo2())
except Exception as e:
    print(e)
