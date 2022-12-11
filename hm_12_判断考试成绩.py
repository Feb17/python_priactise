# 定义整数变量 python_socre, c_score, 编写代码判断成绩

python_score = int(input("请输入python成绩："))
c_score = int(input("请输入C成绩："))
total_score = python_score + c_score
# 只要有一门成绩 >= 60分就算合格

if python_score >= 60 or c_score >= 60:
    print("考试合格, 你的分数为：%d" % total_score)
    if total_score >= 120:
        print("恭喜你，成绩优秀")
else:
    print("考试不合格，继续努力")