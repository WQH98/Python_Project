import requests
import re
from urllib.parse import urljoin

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
# res = requests.get(url, headers=headers)
# data = res.content.decode()  # 抓取页面内容
# with open('闪电侠.html', 'w', encoding='UTF-8') as f:
#     f.write(data)

with open('闪电侠.html', 'r', encoding='UTF-8') as f:
    data = f.read()
# 这是抓取第一次的index.m3u8的地址
index_m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')
# print(index_m3u8_url)

# 进行请求  获取第二次index.m3u8的url地址
# res = requests.get(index_m3u8_url, headers=headers)
# data = res.content.decode()  # 抓取页面内容
# with open('index.m3u8.txt', 'w', encoding='UTF-8') as f:
#     f.write(data)

with open('index.m3u8.txt', 'r', encoding='UTF-8') as f:
    data = f.read()
# print(data.split('/', 3)[-1])
# 拼接第二次请求的m3u8文件地址
# print(index_m3u8_url.rsplit('/', 1)[0]+'/'+data.split('/', 3)[-1].strip())
index_m3u8_url = urljoin(index_m3u8_url, data.split('/', 3)[-1]).strip()
'''
https://new.qqaku.com/20211117/iHVkqQMI/index.m3u8
                     /20211117/iHVkqQMI/2523kb/hls/index.m3u8
https://new.qqaku.com/20211117/iHVkqQMI/2523kb/hls/index.m3u8
https://new.qqaku.com/20211117/iHVkqQMI/2523kb/hls/index.m3u8
https://new.qqaku.com/20211117/iHVkqQMI/2523kb/hls/index.m3u8
'''
# 请求第二个index.m3u8地址，当前返回的内容就是咱们真正获取ts文件的url
res = requests.get(index_m3u8_url, headers=headers)
data = res.content.decode()  # 抓取页面内容
with open('index.m3u8', 'w', encoding='UTF-8') as f:
    f.write(data)