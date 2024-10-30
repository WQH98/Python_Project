# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# 函数fun的参数本来是(s, l)但是l报警告（变量名不明确）
# 最好是不要用I o l来作为变量名 这些字符容易与数字1和0混淆

# str = "abcde"
strs = input("Please enter your str")


def fun(s, le):
    if le == 0:
        return
    print(s[le - 1])
    fun(s, le - 1)


fun(strs, len(strs))
