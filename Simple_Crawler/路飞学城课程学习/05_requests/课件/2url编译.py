import urllib.request
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4&fenlei=256&rsv_pq=b8a56cf200047196&rsv_t=3152txP5Y8PpXqx2dfT1zEfozB%2ByTsi5CLQeEg1LR8A1T6y9w4kXiSWwiNYC&rqlang=en&rsv_enter=1&rsv_dl=tb&rsv_sug3=19&rsv_sug1=22&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=40402&rsv_sug4=40550&rsv_sug=1'
# print(urllib.request.unquote(url))
# print(urllib.request.quote('迪丽热巴'))

url = 'https://www.baidu.com/s?'
kw = {
    'wd': '迪丽热巴'
}
new_url = url + urllib.parse.urlencode(kw)
print(new_url)
res = urllib.request.urlopen(new_url)
print(res.read().decode('UTF-8'))