import re

print(re.search("^1[3-9][0-9]{9}", "13555555555"))

pattern = re.compile("^1[3-9][0-9]{9}")
print(re.search(pattern, "13555555555"))
print(pattern.search("13555555555"))
