import re

# match 只匹配一次 必须从第一位开始 类似于search("^")

print("1", re.match("a", "123456"))
print("2", re.match("[a-z]", "123456"))
print("3", re.match("[a-z]", "123x456"))
print("4", re.match("[a-z][a-z]", "123x456"))
print("5", re.match("[a-z][a-z]", "123x4s56"))
print("6", re.match("[a-z][a-z]", "123xs4s56"))
print("7", re.match("1[3-9][0-9]{9}", "13524525555"))
print("8", re.match("1[3-9][0-9]{9}", "13524525555z"))
print("9", re.match("1[3-9][0-9]{9}", "x13524525555z"))
print("10", re.match("^1[3-9][0-9]{9}", "x13524525555z"))
print("11", re.match("^1[3-9][0-9]{9}", "13524525555z"))
print("12", re.match("^1[3-9][0-9]{9}$", "13524525555z"))
print("13", re.match("^1[3-9][0-9]{9}$", "13524525555"))
print("14", re.match("^1[3-9][0-9]{9}$", "1352452555"))

# 获取匹配的内容
print(re.match("1[3-9][0-9]{9}$", "13524525555").group())
# 等同于
# print(re.match("^1[3-9][0-9]{9}$", "13524525555").group())
