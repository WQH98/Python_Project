# 题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，
# 这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，
# 又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，
# 问海滩上原来最少有多少个桃子？

start = 6
result = 0


def is_start(n):
    for i in range(5):
        n = (n * 5 / 4) + 1
    return n


if __name__ == "__main__":

    while True:
        result = is_start(start)
        if result % 1 == 0:
            break
        else:
            start += 1

    print(result)

