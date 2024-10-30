# 题目：将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。

a = [9, 6, 5, 4, 1, 0]

if __name__ == "__main__":
    # a.reverse()
    # print(a)

    a_len = len(a)
    for i in range(int(a_len / 2.0)):
        a[i], a[a_len - i - 1] = a[a_len - i - 1], a[i]

    print(a)

