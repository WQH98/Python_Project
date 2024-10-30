# 题目：某个公司采用公用电话传递数据，数据是四位的整数，
# 在传递过程中是加密的，加密规则如下：每位数字都加上5,
# 然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

password = 1234

if __name__ == "__main__":
    a = [int(password % 10), int((password % 100) / 10), int((password % 1000) / 100), int(password / 1000)]
    for i in range(4):
        a[i] += 5
        a[i] %= 10
    a[0], a[3] = a[3], a[0]
    a[1], a[2] = a[2], a[1]
    a.reverse()
    print(a)

