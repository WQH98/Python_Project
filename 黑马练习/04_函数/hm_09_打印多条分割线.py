def print_line(char, times):

    print(char * times)


def print_lines(char, times, lines):
    """打印多条分割线"""
    count = 0
    while count < lines:
        count += 1
        print_line(char, times)


print_lines("-", 20, 4)
