# 题目：按相反的顺序输出列表的值。

lista = ["one", "two", "three", "four", "five", "six"]

# lista.reverse()
# print(lista)

for i in range(len(lista)-1, -1, -1):
    print(lista[i])
