import os.path

import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
# 读取index.m3u8文件  以列表形式返回每一行
with open('index.m3u8', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
path = 'ts'  # 下载所有ts的文件的路径
if not os.path.exists(path):
    os.mkdir(path)
# print(lines)
# 循环读取每一行数据
i = 0
for line in lines:
    # 获取所有要下载的ts的url地址  不以#作为开头
    if line.startswith('#'):
        continue
    # print(line)
    # 进行下载处理
    url = line.strip()  # 去除请求的url中可能包含的其他的字符
    res = requests.get(url, headers=headers)
    # 拼接下载文件的路径及下载后ts的文件名称
    file_path = os.path.join(path, str(i)+'.ts')
    # 进行下载写入
    with open(file_path, 'wb') as f:
        f.write(res.content)
    i += 1