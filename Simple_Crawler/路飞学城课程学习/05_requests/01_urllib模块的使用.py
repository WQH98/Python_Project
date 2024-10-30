import urllib.request

url = 'http://www.baidu.com'

# 请求网址
res = urllib.request.urlopen(url)
# print(res)
# print(type(res))
# 获取响应的状态码
# print(res.getcode())
# 获取请求的url地址
# print(res.geturl())
# 获取请求头
# print(res.getheaders())
# 获取代码返回的数据
# print(res.read().decode('utf-8'))
# 下载
urllib.request.urlretrieve('https://inews.gtimg.com/om_bt/OjPq2cnMN_-ivDKjxpCZ2kk_ab8YC5VMnL-0pQ21fUvd4AA/1000', filename='./download_file/01_xd.jpg')

