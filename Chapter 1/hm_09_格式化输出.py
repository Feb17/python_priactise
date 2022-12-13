# 定义字符串变量name，输出 ”我的名字叫 小明， 请多多关照！“
name = input("请输入你的名字: ")
print("我的名字叫%s，请多多关照！" % name)

# 定义整数变量student_no，输出 我的学号是000001
student_no = int(input("请输入你的学号: "))
print("我的学号是：%06d" % student_no)  # %06d 不足6位补足，>=6位则实际显示

# 定义小数 price, weight, money
# 输出
price = float(input("苹果单价："))
weight = float(input("购买重量："))
money = price * weight
print("苹果单价 %.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))

# 定义一个小数scale，输出 数据比例是25.00%
scale = 0.25
print("数据比例是%.2f%%" % (scale * 100))