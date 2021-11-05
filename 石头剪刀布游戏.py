import random

def main():
    a = 0
    x = random.randint(0,2)
    while True:
        try:
            if a != 0 and a != 1 and a !=2:
                a = int(input("请输入： 剪刀（0），石头（1）， 布（2）: "))
        except ValueError:
                print("请输入0 - 2 之间的一个数字！")
                continue
        except IndexError:
                print("请输入0 - 2 之间的一个数字！")
        if a == x:
            print("平局")
        elif a == 0 and x == 1:
            print("你输啦")
        elif a == 0 and x == 2:
            print("你赢啦")
        elif a == 1 and x == 0:
            print("你赢啦")
        elif a == 1 and x == 2:
            print("你输啦")
        elif a == 2 and x == 0:
            print("你输啦")
        elif a == 2 and x == 1:
            print("你赢啦")
        else:
            print("请输入0 - 2 之间的一个数字！")

if __name__ == '__main__':
    main()
