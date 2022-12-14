def print_line(chart, times):
    """打印单行分隔线

    :param chart: 分割线使用的分隔字符
    :param times: 分割字符重复的次数
    """
    print(chart * times)


def print_lines(chart, times, rows):
    """打印多行分隔线

    :param rows: 需要打印的行数
    :param chart: 分割线使用的分隔字符
    :param times: 分割字符重复的次数
    """
    while rows > 0:
        print_line(chart, times)
        rows -= 1


name = "程序员"
