# 定义 holiday_name 字符串变量，记录节日名称

holiday_name = input("请输入节日：")

if holiday_name == "情人节":
    print("买玫瑰")
    print("看电影")
elif holiday_name == "平安夜":
    print("买苹果")
elif holiday_name == "生日":
    print("买蛋糕")

else:
    print("每天都是节日")