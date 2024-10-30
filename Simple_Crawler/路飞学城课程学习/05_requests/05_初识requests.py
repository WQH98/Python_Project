import requests

# 开始get请求
url = 'http://www.baidu.com'
res = requests.get(url)

# 获取响应
# print(res)
# print(type(res))

# 获取请求的url
# print(res.url)

# 获取响应的内容 会使用默认编码 有时候会乱码 需要指定编码
# print(res.encoding)  # 获取当前编码
# res.encoding = 'utf-8'    # 设置当前编码
# print(res.text)    # 获取响应内容

# 获取文本的另外一种方式
# print(res.content.decode('utf-8'))


# 获取状态码
# print(res.status_code)
# 获取响应对应的请求头
# print(res.request.headers)
# 获取响应对应的cookies
# print(res.cookies)


