import re

objs = re.finditer("[a-z]", "abcdefg")
for obj in objs:
    print(obj)
    print(obj.group())

