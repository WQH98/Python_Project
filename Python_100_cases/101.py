# 题目： 获取 100 以内的质数。
# 程序分析：质数（prime number）又称素数，有无限个。
# 质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为质数，
# 如：2、3、5、7、11、13、17、19。

num = []
flag = 0

if __name__ == "__main__":
    for i in range(2, 100):
        for j in range(2, i):
            if (i != j) and (i % j == 0):
                flag = 1
                break
        if flag == 0:
            num.append(i)
        flag = 0
    print(num)
