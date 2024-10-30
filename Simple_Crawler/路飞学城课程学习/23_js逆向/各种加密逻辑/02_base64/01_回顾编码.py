'''
    http协议想要发送字符串 非常麻烦 所以程序员就发明了一个
    能把二进制字节转换成字符串的机制 发送请求的时候 不再传输
    字节了 改成传输字符串 目前市面上最常见的就是base64
    由64个符号组成 a-z A-Z 0-9 + /
    填充的逻辑是 在最终末尾添加= =的个数不会超过3个
'''

import base64
s = 'hello world'
# 加密(模拟) 结果一定是字符串
bs = s.encode('utf-8')
# 把字节处理成base64字符串
xxx = base64.b64encode(bs)
# decode以后的每一个字节 都在ASCII码的范围里
# 所以decode中不需要加参数
print(xxx.decode())
# 每4位组成三个字节 最后使用=填充 所以个数一定能被4整除
print(len(xxx) / 4)

res = base64.b64decode(xxx).decode("utf-8")
print(res)

