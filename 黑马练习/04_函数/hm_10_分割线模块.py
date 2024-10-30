def print_line(char, times):
    """打印一条分割线"""
    print(char * times)


def print_lines(char, times, lines):
    """打印多条分割线"""
    count = 0
    while count < lines:
        count += 1
        print_line(char, times)


name = "王庆浩"
