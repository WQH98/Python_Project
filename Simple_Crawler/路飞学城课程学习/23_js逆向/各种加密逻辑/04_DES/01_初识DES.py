from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import base64

# 以下步骤是固定的
s = "alex昨天吃多了"
# 1、先创建加密器
# DES要求的key和IV的长度都是8字节
des = DES.new(key="abcdefgh".encode(), mode=DES.MODE_CBC, IV=b'01234567')

# 2、加密或者解密 需要的参数是字节
# DES在模式CBC key长度为8的情况下 需要加密的字节数需要是8的倍数
# 不够位数则需要填充
bs = s.encode("utf-8")
# bs = pad(bs, DES.block_size)
# 常规情况下填充的倍数都是8
bs = pad(bs, 8)
res = des.encrypt(bs)
# 加密后的东西是无法用肉眼看出来它是什么的 也不能处理成utf-8
# 在网页上通常都会把这种字节转换成base64 方便数据的传输
# 现在的res是字节 需要转换成字符串
res = base64.b64encode(res)
res = res.decode()
print(res)

# 下面将base64字符串 转换成正常的数据
bs = base64.b64decode(res)

# 对字节进行解密
des1 = DES.new(key="abcdefgh".encode(), mode=DES.MODE_CBC, IV=b'01234567')
bs = des1.decrypt(bs)
bs = unpad(bs, 8)
bs = bs.decode('utf-8')
print(bs)


