# 题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# E:\code\Python_Pro\Python_100_cases\097.txt

if __name__ == "__main__":
    filename = input("please enter a filename: ")
    fp = open(filename, "w+")
    ch = input("please enter a character: ")
    while ch != '#':
        fp.write(ch)
        ch = input("please enter a character: ")
    fp.close()
