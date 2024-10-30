# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。

s = input("please enter str: ")
i = 0
yingyu = 0
kongge = 0
shuzi = 0
qita = 0

while i < len(s):
    if s[i].isalpha():
        yingyu += 1
    elif s[i].isdigit():
        shuzi += 1
    elif s[i].isspace():
        kongge += 1
    else:
        qita += 1
    i += 1

print('char = %d, space = %d, digit = %d, others = %d' % (yingyu, kongge, shuzi, qita))
