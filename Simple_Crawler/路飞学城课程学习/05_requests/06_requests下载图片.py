import requests

url = 'https://img10.360buyimg.com/n1/jfs/t21757/253/1694149328/94678/2c52d8fc/5b305680Na2e1d2bd.jpg'

# 请求
res = requests.get(url)

# 写入
with open('./download_file/02_cx.jpg', 'wb') as f:
    # 写入文件   注意：必须为二进制形式
    f.write(res.content)

