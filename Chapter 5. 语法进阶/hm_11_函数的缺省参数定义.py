# gender=True 指定缺省参数，指定缺省参数必须在参数列表的末尾！！！
def print_info(name, title="", gender=True):
    """
    判断班上同学的性别
    :param title: 职位
    :param name: 姓名
    :param gender: 性别 True = 男生；False = 女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s]%s 是 %s" % (title, name, gender_text))


print_info("小明")
print_info("小美", gender=False)
