from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

# 1、弄个加密器
# 需要提前准备好RSA Key
# 读取公钥内容
f = open('./01_密钥/pub_key.pem', mode='r', encoding='utf-8')
# 处理成RSA Key
rsa_key = RSA.importKey(f.read())
f.close()
# print(type(rsa_key))

rsa = PKCS1_v1_5.new(key=rsa_key)
s = 'alex特别喜欢sb'
# 进行数据加密
r = rsa.encrypt(s.encode('utf-8'))
# 将结果处理成base64 方便进行传输
r = base64.b64encode(r).decode()
print(r)

# 2、弄个解密器
f = open('./01_密钥/pri_key.pem', mode='r', encoding='utf-8')
# 读取私钥内容 处理成RSA Key
rsa_key = RSA.importKey(f.read())
f.close()
rsa = PKCS1_v1_5.new(key=rsa_key)
# 进行解密
r = base64.b64decode(r)
r = rsa.decrypt(r, None)
print(r.decode('utf-8'))

