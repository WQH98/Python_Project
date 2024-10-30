import re

str = "abcd1"

print(re.search("(\\d+)", str).group())
print(re.search("(?P<number>\\d+)", str).group())
# 当有多个子存储的时候 使用别名比较方便
print(re.search("(\\d+)", str).group(0))
print(re.search("(?P<number>\\d+)", str).group("number"))
