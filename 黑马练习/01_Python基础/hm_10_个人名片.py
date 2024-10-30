# 在控制台依次提示用户输入：姓名、公司、职位、电话、邮箱
# 按照以下格式输出
"""
公司名称：

姓名（职位）

电话：
邮箱：
"""

name = input("请输入姓名：")
company = input("请输入公司：")
position = input("请输入职位：")
number = input("请输入电话：")
postbox = input("请输入邮箱：")

print("*" * 50)
print("公司名称：%s" % company)
print()
print("姓名：%s（职位：%s）" % (name, position))
print()
print("电话：%s" % number)
print("邮箱：%s" % postbox)
print("*" * 50)