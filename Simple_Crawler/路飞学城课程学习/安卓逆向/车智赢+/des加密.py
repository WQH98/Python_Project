import base64
from Crypto.Cipher import DES3


BS = 8
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

# DES3的MODE_CBC模式下只有前24位有意义
key = b"appapiche168comappapiche168comap"[0: 24]
iv = b"appapich"

plaintext = pad("xxxxxx").encode("utf-8")

# 使用MODE_CBC创建cipher
cipher = DES3.new(key, DES3.MODE_CBC, iv)
result = cipher.encrypt(plaintext)
res = base64.b64encode(result)
print(res)
