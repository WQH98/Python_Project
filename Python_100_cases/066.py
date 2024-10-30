# 题目：输入3个数a,b,c，按大小顺序输出。　　

if __name__ == "__main__":
    num1 = int(input("num1 = "))
    num2 = int(input("num2 = "))
    num3 = int(input("num3 = "))

    if num1 < num2:
        num1, num2 = num2, num1
    if num1 < num3:
        num1, num3 = num3, num1
    if num2 < num3:
        num2, num3 = num3, num2

    print(num1, num2, num3)
