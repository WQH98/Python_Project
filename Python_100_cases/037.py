# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，
# 下次类推，即用第二个元素与后8个进行比较，并进行交换。

N = 10
array = []
if __name__ == "__main__":

    for i in range(10):
        tmp = int(input("Enter a number: "))
        array.append(tmp)

    print(array)
    # array.sort()
    # print(array)

    for i in range(10 - 1):
        for j in range(i+1, 10):
            if array[i] > array[j]:
                # tmp = array[i]
                # array[i] = array[j]
                # array[j] = tmp
                array[i], array[j] = array[j], array[i]


    print(array)
