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
# 获取请求返回的数据
# print(res.read().decode('utf-8'))
# 下载
url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fp5.itc.cn%2Fq_70%2Fimages01%2F20210827%2F62444c25b3e244c988930c892b42fc0b.jpeg&refer=http%3A%2F%2Fp5.itc.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662728415&t=6f1a4221d010b579718ba6bf2d1a1696'
urllib.request.urlretrieve(url, filename='bnl.jpg')
