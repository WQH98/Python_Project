from hashlib import md5

#  可以加盐 为了防止撞库
obj = md5(b"sadhuahduiahdiada")
s = "alex"
obj.update(s.encode('utf-8'))
# 固定的 得到32位16进制的数字
val = obj.hexdigest()
print(val)

