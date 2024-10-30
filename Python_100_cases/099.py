# 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
# E:\code\Python_Pro\Python_100_cases\099_A.txt
# E:\code\Python_Pro\Python_100_cases\099_B.txt
# E:\code\Python_Pro\Python_100_cases\099_C.txt


if __name__ == "__main__":
    filenameA = "E:\\code\\Python_Pro\\Python_100_cases\\099_A.txt"
    filenameB = "E:\\code\\Python_Pro\\Python_100_cases\\099_B.txt"
    filenameC = "E:\\code\\Python_Pro\\Python_100_cases\\099_C.txt"

    fp = open(filenameA, "r+")
    strA = fp.read()
    fp.close()
    fp = open(filenameB, "r+")
    strB = fp.read()
    fp.close()
    strC = strA + strB
    fp = open(filenameC, "w+")
    fp.write(strC)
    fp = open(filenameC, "r+")
    print(fp.read())
    fp.close()
