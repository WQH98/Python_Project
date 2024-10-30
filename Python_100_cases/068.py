# 题目：有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
# 思路：用到了列表切片操作（更简单）
# lst[start:end:step]
# 其中start表示起始位置（包括该位置），end表示结束位置（不包括该位置），step表示步长。

# 使用切片
num_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

if __name__ == "__main__":
    m = int(input("Please enter m: "))
    num1_array = num_array[:m]
    num2_array = num_array[m:]
    for i in range(m):
        num2_array.append(num1_array[i])
    print(num2_array)


# 切片操作示例代码
# lst = [1, 2, 3, 4, 5]
# # 选取第2个到第4个元素
# print(lst[1:4])  # [2, 3, 4]
#
# # 选取第2个元素到列表结尾的元素
# print(lst[1:])  # [2, 3, 4, 5]
#
# # 选取列表的前3个元素
# print(lst[:3])  # [1, 2, 3]
#
# # 反向遍历整个列表
# print(lst[::-1])  # [5, 4, 3, 2, 1]
