import re

str = "abc\r1d2\te3\nfg"

# 按照数字进行拆分
print(re.split('\\d', str))
print(re.split('\\d', str, maxsplit=2))

# 匹配空白符
print(re.findall('\\s', str))
print(re.findall('\\S', str))

# 按照空白符进行拆分
print(re.split("\\s", str))
