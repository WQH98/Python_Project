# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

liat_a = [1, 2, 3, 5, 6, 8, 10]

if __name__ == '__main__':
    ins = int(input("Enter a number: "))
    for i in range(len(liat_a)):
        if ins < liat_a[i]:
            liat_a.insert(i, ins)
            break
    print(liat_a)

