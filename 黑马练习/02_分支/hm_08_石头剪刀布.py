import random
# 1.从控制台输入要出的拳----石头（1）/剪刀（2）/布（3）
player = int(input("输入要出的拳----石头（1）/剪刀（2）/布（3）:"))
player_sign = "石头"
if (player < 1) or (player > 3):
    print("输入错误，请重新输入！！！")
    exit()
if player == 1:
    player_sign = "石头"
elif player == 2:
    player_sign = "剪刀"
elif player == 3:
    player_sign = "布"
else:
    exit()
print("玩家出的拳是%s" % player_sign)
# 2.电脑随机出拳----先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1, 3)
computer_sign = "石头"
if computer == 1:
    computer_sign = "石头"
elif computer == 2:
    computer_sign = "剪刀"
elif computer == 3:
    computer_sign = "布"
else:
    exit()
print("电脑出的拳是%s" % computer_sign)
# print("玩家出的拳是",player_sign,"电脑出的拳是",computer_sign)
# 3.比较胜负
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("玩家胜！！！")
elif player == computer:
    print("平局！！！")
else:
    print("电脑胜！！！")
