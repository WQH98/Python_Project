# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

num_array = [0, 3, 3, 2, 5, 7, 4, 3, 23, 2, 7, 1]

if __name__ == '__main__':
    max_index = num_array.index(max(num_array))
    num_array[0], num_array[max_index] = num_array[max_index], num_array[0]
    min_index = num_array.index(min(num_array))
    num_array[len(num_array) - 1], num_array[min_index] = num_array[min_index], num_array[len(num_array) - 1]
    print(num_array)

