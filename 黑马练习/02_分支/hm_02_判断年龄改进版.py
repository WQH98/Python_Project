while 1:
    # 1.输入用户年龄
    age = int(input("请输入年龄："))
    # 2.判断是否满18岁
    # 3.如果满18岁，允许进网吧happy
    if age >= 18:
        print("允许进网吧happy")
    # 4.如果未满18岁，提示回家写作业
    else:
        print("回家写作业")
