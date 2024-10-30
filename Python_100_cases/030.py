# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

start = int(input("enter the number: "))
start_tmp = start
array = []

for i in range(5):
    array.append(start_tmp % 10)
    start_tmp = int(start_tmp / 10)


if(array[0] == array[4]) and (array[1] == array[3]):
    print("%d is palindromic number" % start)
else:
    print("%d is not palindromic number" % start)

