# 1.定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 2.定义整形变量 knife_length 表示刀的长度，单位：厘米
knife_length = -10
# 3.首先检查是否有车票，如果有，才允许进行安检
if has_ticket:
    print("有车票，可以进行安检！！！")
    # 4.安检时，需要检查刀的长度，判断是否超过20厘米
    # 如果超过20厘米，提示刀的长度，不允许上车
    # 如果不超过20厘米，安检通过
    if knife_length > 20:
        print("您的刀有%d厘米，超过了20厘米，禁止进门！！！" % knife_length)
    else:
        print("可以上车！！！")
# 5.如果没有车票，不允许进门
else:
    print("无车票，禁止进门！！！")