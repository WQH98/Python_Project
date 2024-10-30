# 题目：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

a = []
result = 0

if __name__ == '__main__':
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(int(input("Please enter a number: ")))

    for i in range(3):
        result += a[i][i]

    print(result)

