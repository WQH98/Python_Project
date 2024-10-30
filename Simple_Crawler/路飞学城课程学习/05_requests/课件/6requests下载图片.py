import requests

url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171202%2F0184f9ea5b7448bd8721fa8110dd885f.jpeg&refer=http%3A%2F%2F5b0988e595225.cdn.sohucs.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662731311&t=c1b3ec1844363ecf73e16ac5b10fa9b1'
# 请求
res = requests.get(url)
# 写入
with open('nk400.jpg', 'wb') as f:
    # 写入文件  注意：必须为二进制形式
    f.write(res.content)
