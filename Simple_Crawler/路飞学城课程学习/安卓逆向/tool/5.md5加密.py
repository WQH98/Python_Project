import hashlib

# 明文
str_data = "12345678900"

obj = hashlib.md5()
obj.update(str_data.encode("utf-8"))
hex_string = obj.hexdigest()
print(hex_string)

"""
明文 
密文 
"""

