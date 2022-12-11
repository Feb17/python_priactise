import random

'''
class numExceptionError(Exception):
    def __init__(self, ErrorInfo="请输入0 - 2 之间的一个数字"):
        super().__init__(self) # 初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        print(self.errorinfo)
        #return self.errorinfo
'''


def main():
    a = 0
    while True:
        try:
            a = int(input("请输入： 剪刀（0），石头（1）， 布（2）: "))
            if a < 0 or a > 2:
                print("请输入0 - 2 之间的一个数字")
        except Exception as e:
            print("请输入0 - 2 之间的一个数字")
        else:
            x = random.randint(0, 2)
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


if __name__ == '__main__':
    main()
