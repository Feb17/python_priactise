poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t 更上一层楼"

print(poem_str)

# 1. 拆分字符串
poem_list = poem_str.split()

print(poem_list)

# 2. 拼接字符串
poem_list2 = "\n".join(poem_list)
print(poem_list2)
