import requests

url = 'https://www.pearvideo.com/videoStatus.jsp'

params = {
    'contId': '1793469',
    'mrd': '0.19761111180222302'
}

headers = {
    'Cookie': 'tgw_l7_route=c94993c99ec065901a2ef1434ac92da5; JSESSIONID=119A571508403691A16D29916614662F; PEAR_UUID=8236376d-6e1c-4550-b338-8bce7a67e914; _uab_collina=171299725109436956020138; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1712997252; p_h5_u=9BD5B115-059B-4FFB-90AA-AA3010429383; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1712997255',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.pearvideo.com',
    'Referer': 'https://www.pearvideo.com/video_1793469'
}

res = requests.get(url, headers=headers, params=params)
systemTime = res.json()['systemTime']
mp4_url = res.json()['videoInfo']['videos']['srcUrl'].replace(systemTime, "cont-1793469")
print(mp4_url)

headers = {
    'Cookie': 'PEAR_UUID=8236376d-6e1c-4550-b338-8bce7a67e914; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1712997252; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1712997266',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'Referer': 'https://www.pearvideo.com/'
}

res = requests.get(mp4_url)
with open('./08_梨视频.mp4', 'wb') as f:
    f.write(res.content)




