# 题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。

import time
import random

if __name__ == "__main__":
    play_it = input("do you want to play it.(\'y\' or \'n\')")
    while (play_it == 'y') or (play_it == 'Y'):
        i = random.randint(0, 2**32) % 100
        start = time.perf_counter()
        a = time.time()
        guess = int(input("input your guess: "))
        while guess != i:
            if guess > i:
                print("please input a little smaller")
            else:
                print("please input a little bigger")
            guess = int(input("input your guess: "))
        end = time.perf_counter()
        b = time.time()
        var = (end - start) / 18.2
        print(var)
        if var < 15:
            print("you are very clever!")
        elif var < 25:
            print("you are normal!")
        else:
            print("you are stupid!")
        print("Congratulations")
        print("The number you guess is %d" % i)

        play_it = input('do you want to play it.')

