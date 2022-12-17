students_list = [{"name": "阿土",
                  "age": 20,
                  "gender": True,
                  "height": 170,
                  "weight": 75},
                 {"name": "小美",
                  "age": 19,
                  "gender": False,
                  "height": 160,
                  "weight": 45}]

find_name = str(input("请输入需要查询的名称："))

for students_name in students_list:
    # print(students_name)
    if students_name["name"] == find_name:
        print("找到%s了" % find_name)
        print("%s的信息如下：%s" % (find_name, students_name))
        break
else:
    print("抱歉，没有找到%s的相关信息" % find_name)


