# 题目：一个球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
# 求它在第10次落地时，共经过多少米？第10次反弹多高？
# 程序分析：无

a = 100
tour = []

for i in range(10):
    a /= 2
    tour.append(a)
    tour.append(a)

print(sum(tour) + 100 - a - a)

print(a)
