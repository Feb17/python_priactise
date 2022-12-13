import random
player = int(input("请输入你要出 石头/剪刀/布？"))
computer = random.randint(1, 3)

print("你出的是 %d - 电脑出的是 %d" % (player, computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("你赢啦")

elif player == computer:
    print("平局")

else:
    print("你输了")
