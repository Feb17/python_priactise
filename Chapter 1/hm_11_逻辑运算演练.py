# 定义一个整数变量 age
age = int(input("请输入年龄："))

# 要求人的年龄在 0-120 之间
if age >= 0 and age <= 120: # 0 <= age <= 120
    print(age)
else:
    print("年龄不正确")
