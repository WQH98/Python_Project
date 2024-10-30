# 题目：八进制转换为十进制
# ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，
# 它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，
# 如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。
# 语法 ord(c)  c -- 字符
# 返回值是对应的十进制整数


if __name__ == "__main__":
    p = "122"
    n = 0
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print(n)
