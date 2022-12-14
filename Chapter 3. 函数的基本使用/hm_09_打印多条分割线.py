import hm_08_打印分割线


def print_lines(chars, times, rows):
    """打印多行分隔线

    :param rows: 需要打印的行数
    :param chars: 分割线使用的分隔字符
    :param times: 分割字符重复的次数
    """
    while rows > 0:
        hm_08_打印分割线.print_line(chars, times)
        rows -= 1


print_lines("-", 20, 5)
