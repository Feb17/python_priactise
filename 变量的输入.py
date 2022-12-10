# 1.输入苹果单价
price_str = input("苹果的单价")

# 2.输入苹果的质量
weight_str = input("苹果的重量")

# 3.计算支付的金额
money = float(price_str) * float(weight_str) #字符串变量转换成浮点型

print(money)