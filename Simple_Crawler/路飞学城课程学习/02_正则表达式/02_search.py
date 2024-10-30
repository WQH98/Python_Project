import re

# search 只匹配一次


print(re.search("a", "123456"))
print(re.search("[a-z]", "123456"))
print(re.search("[a-z]", "123x456"))
print(re.search("[a-z][a-z]", "123x456"))
print(re.search("[a-z][a-z]", "123x4s56"))
print(re.search("[a-z][a-z]", "123xs4s56"))
print(re.search("1[3-9][0-9]{9}", "13524525555"))
print(re.search("1[3-9][0-9]{9}", "13524525555z"))
print(re.search("1[3-9][0-9]{9}", "x13524525555z"))
print(re.search("^1[3-9][0-9]{9}", "x13524525555z"))
print(re.search("^1[3-9][0-9]{9}", "13524525555z"))
print(re.search("^1[3-9][0-9]{9}$", "13524525555z"))
print(re.search("^1[3-9][0-9]{9}$", "13524525555"))
print(re.search("^1[3-9][0-9]{9}$", "1352452555"))

# 获取匹配的内容
print(re.search("^1[3-9][0-9]{9}$", "13524525555").group())



