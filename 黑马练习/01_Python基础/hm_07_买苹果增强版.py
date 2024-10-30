# 收银员输入苹果的价格，单位：元/斤
price = float(input("请输入苹果单价："))

# 收银员输入用户购买苹果的重量，单位：斤
weight = float(input("请输入苹果重量："))

# 计算并且输出付款金额
money = price * weight
print("请支付%.2f元" % money)

# print(money)
