import requests

url = 'https://xueqiu.com/statuses/hot/listV3.json?page=2&last_id=285618131'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'Referer': 'https://xueqiu.com/',
    'Host': 'xueqiu.com',
    'Cookie': 'acw_tc=2760779d17128407494834611e12106cc80d337e1ba8d31faefd2b0a199f77; xq_a_token=4b8bc7136c9fd7b4395f9ca0a65c38363243df2b; xqat=4b8bc7136c9fd7b4395f9ca0a65c38363243df2b; xq_r_token=3f230866347670b258c76aecd81456e63e6aa98b; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcxNDk1NjQ2MiwiY3RtIjoxNzEyODQwNzI0NDU0LCJjaWQiOiJkOWQwbjRBWnVwIn0.OLUiG7BA4Be28YDQzuEvooeUOan7Uvnk-u6lBNe-gLHiH43CC1jTzaxxVoaSSkQa9aRCNojd2G6B1kA4oPvSxSi_CEfCa25sDr8l948xDMswONSECQPXy1apARkK7bnbHBb-AZg4ilem9uBEK_3k7DnLNmupI3tHycfLfODnKGAjOg37cfKneSekuDUf4YL7pm-Mtp423yvTfP_HWFZcNiWM9O4H_IIOyRwjla6T3QeuKdKFkEPU4lZljQXuRSsl5mI321I_oMrkBdCTHFmnhFOC7IifkmFIUSTP4fAg-NTB1fSZvmttMBlAf4RaZ5mSRFPa3QWIffjd2K6WKK3MmA; cookiesu=751712840749512; u=751712840749512; device_id=f64f6d0f6799d0013e84f8a699a85d69; Hm_lvt_1db88642e346389874251b5a1eded6e3=1712840751; smidV2=2024041121055135f629315e7d593442c2ce455548ce2c00382fea0109dc190; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1712840809; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=s3epu3zQQXiZsIEDHpArSLeKWR6iEhDwz8a5pf6klv5fYTV6L1osIFFmtB2FRQdq3jOe52WghK/dCePTx1fbhQ%3D%3D'
}


response = requests.get(url, headers=headers)

print(response.json())
