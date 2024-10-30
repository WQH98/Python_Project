from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import base64

# 以下步骤是固定的
s = "alex昨天吃多了"
# 1、先创建加密器
# 对于key的要求是 必须是字节 所以可以写成下面两种方式
# mode 要么是ECB 要么是CBC 这两种模式占了99.99%
# 这两种模式的区别是
# ECB 不用给偏移量IV
# CBC 需要给出偏移量IV
# aes = AES.new(key=b"abcdefghijklmn12")
# 因为key里面都是ascii码的内容 所以encode中不需要加参数
aes = AES.new(key="abcdefghijklmn12".encode(), mode=AES.MODE_ECB)

# 2、加密或者解密 需要的参数是字节
# AES在模式ECB key长度为16的情况下 需要加密的字节数需要是16的倍数
# 不够位数则需要填充
bs = s.encode("utf-8")
# bs = pad(bs, AES.block_size)
# 常规情况下填充的倍数都是16
bs = pad(bs, 16)
res = aes.encrypt(bs)
# 加密后的东西是无法用肉眼看出来它是什么的 也不能处理成utf-8
# 在网页上通常都会把这种字节转换成base64 方便数据的传输
# 现在的res是字节 需要转换成字符串
res = base64.b64encode(res)
res = res.decode()
print(res)

# 下面将base64字符串 转换成正常的数据
bs = base64.b64decode(res)

# 对字节进行解密
aes1 = AES.new(key="abcdefghijklmn12".encode(), mode=AES.MODE_ECB)
bs = aes1.decrypt(bs)
bs = unpad(bs, 16)
bs = bs.decode('utf-8')
print(bs)


