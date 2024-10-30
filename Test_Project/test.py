

def dijigezifu():
    str1 = "2022032817491234"
    for i in range(len(str1)):
        print(f"第{i + 1}个字节" + str1[i])


def shuzihuanhang():
    str1 = "01 02 41 0B 44 4C 2D 54 72 61 63 6B 4F 75 74 01 01 01 02 41 07 55 73 65 72 34 35 36 41 10 32 30 32 33 30 32 31 30 31 35 33 35 35 39 31 36"
    list1 = str1.split(" ")
    print(f"共{len(list1)}个数据")
    for i in list1:
        print(i)


dijigezifu()
