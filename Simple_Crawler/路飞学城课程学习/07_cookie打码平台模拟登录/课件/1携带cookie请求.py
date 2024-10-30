import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'Cookie': 'acw_tc=2760826216605661451391678e6500fd50e00f610e2712bc899e790f170526; s=c515m3bdl5; xq_a_token=28ed0fb1c0734b3e85f9e93b8478033dbc11c856; xq_r_token=bf8193ec3b71dee51579211fc4994d03f17c64ac; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY2MzExMzIyMSwiY3RtIjoxNjYwNTY2MTIzMjA5LCJjaWQiOiJkOWQwbjRBWnVwIn0.atjGTIMW1M8kaW0UWPGX01KhhaQsBJg3lZItX-jmBJ226WGwpqxoZ2ftdLJ_2sURRFCNpL0MoZX-7l_-gRFX9j857MCBoAMCzRBMVE4yL8HLTGsNRmhX5IThnAix5XUKU4dMRcdh66tiM-Bhy_uSaHbeN62dGZvDpb3wkdY5QUexKjPVvIO6c3_DW09uFBvRQLfVhMT2AZUEN-Lio5w-WSRiUJp5GXddilJqrxdGlKctA8zBhBwZveVhTXYLE8R1hcctuW-hCHCXvUBRgD3-ZIaW9WrKSeV_Y-9IiuQmjapwnBOClY1b7jfhHT4u83rUXU_0grzc1qWKcWFdpEpNKg; u=271660566146135; cookiesu=271660566146135; Hm_lvt_1db88642e346389874251b5a1eded6e3=1660566147; device_id=be2627c81c6f6532c44c2bfa4f85108e; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1660566228'
}
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=384373&size=15'
res = requests.get(url, headers=headers)
print(res.status_code)
print(res.json())