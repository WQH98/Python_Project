# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# E:\code\Python_Pro\Python_100_cases\098.txt

if __name__ == "__main__":
    filename = input("please enter a filename: ")
    fp = open(filename, "w+")
    str1 = input("Please enter a str: ")
    str1 = str1.upper()
    fp.write(str1)
    fp = open(filename, "r+")
    print(fp.read())
    fp.close()
