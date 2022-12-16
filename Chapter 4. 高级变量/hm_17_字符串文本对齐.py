poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.center(10, "　"))

for poem_str in poem:
    print("|%s|" % poem_str.ljust(10, "　"))

poem2 = ["\t\n登鹳雀楼",
         "王之涣",
         "白日依山尽\t\n",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]

for poem_str2 in poem2:
    print("|%s|" % poem_str2.strip().center(10, "　"))
