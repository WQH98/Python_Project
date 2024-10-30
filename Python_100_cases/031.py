# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
# 星期天 Sunday
# 星期一 Monday
# 星期二 Tuesday
# 星期三 Wednesday
# 星期四 Thursday
# 星期五 Friday
# 星期六 Saturday

first_number = input("Please enter the first number: ")
if first_number == 'm':
    print("Monday")
elif first_number == 'f':
    print("Friday")
elif first_number == 'w':
    print("Wednesday")
elif first_number == 't':
    second_number = input("Please enter the second number: ")
    if second_number == 'u':
        print("Tuesday")
    elif second_number == 'h':
        print("Thursday")
elif first_number == 's':
    second_number = input("Please enter the second number: ")
    if second_number == 'u':
        print("Sunday")
    elif second_number == 'a':
        print("Saturday")
