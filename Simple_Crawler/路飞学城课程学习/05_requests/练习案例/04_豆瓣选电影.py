import json
import requests

url = 'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=0&count=20&selected_categories=%7B%7D&uncollect=false&tags=2024'

headers = {
    'Cookie': 'bid=gvQ8mPrN9Sw; viewed="36206031_36661132"; ap_v=0,6.0; __utma=30149280.1546279071.1710924113.1712543429.1712665088.5; __utmb=30149280.0.10.1712665088; __utmc=30149280; __utmz=30149280.1712665088.5.4.utmcsr=localhost:63342|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'Host': 'm.douban.com',
    'Origin': 'https://movie.douban.com',
    'Referer': 'https://movie.douban.com/explore',
    'Sec-Ch-Ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors'
}

res = requests.get(url, headers=headers)




