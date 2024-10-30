# 题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数

def move(array, m, n):
    array_end = array[n - 1]
    for i in range(n - 1, -1, -1):
        array[i] = array[i - 1]
    array[0] = array_end
    m -= 1
    if m > 0:
        move(array, m, n)


if __name__ == "__main__":
    n = int(input("Please enter n: "))
    m = int(input("Please enter m: "))
    num_array = []
    for i in range(n):
        num_array.append(int(input("Enter a number: ")))
    print("begin: ", num_array)
    move(num_array, m, n)
    print("after: ", num_array)
