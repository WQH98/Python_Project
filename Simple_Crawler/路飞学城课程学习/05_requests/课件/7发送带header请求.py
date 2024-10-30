import requests

url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fwww.ducatichina.cn%2Fwp-content%2Fuploads%2F2021%2F02%2F0c8dc0d3d9e438be620f2bb1dd4c165-scaled.jpg&refer=http%3A%2F%2Fwww.ducatichina.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1662731843&t=62a94c4ab884f7459829900f92f4bf4d'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# 请求
res = requests.get(url, headers=headers)
# 写入
with open('dukadi.jpg', 'wb') as f:
    # 写入文件  注意：必须为二进制形式
    f.write(res.content)