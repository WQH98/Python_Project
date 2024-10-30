# 1.定义 holody_name 字符串变量记录节日名称
holody_name = str(input("请输入节日名称："))
# 2.如果是 情人节 应该买玫瑰/看电影
if holody_name == "情人节":
    print("买玫瑰 看电影！！！")
# 3.如果是 平安夜 应该吃苹果/吃大餐
elif holody_name == "平安夜":
    print("买苹果 吃大餐！！！")
# 4.如果是 生日 应该买蛋糕
elif holody_name == "生日":
    print("买蛋糕！！！")
# 5.其他的日子每天都是节日啊
else:
    print("其他的日子每天都是节日啊！！！")


