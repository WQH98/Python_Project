i = 0

while i < 10:
    if i == 3:
        # continue 关键字某一条件满足时，不执行后续重复的代码
        # 注意：再循环中，如果使用continue这个关键字
        # 在使用关键字之前，需要确认循环的计数是否修改，否则可能会造成死循环
        continue
    print(i)
    i += 1
