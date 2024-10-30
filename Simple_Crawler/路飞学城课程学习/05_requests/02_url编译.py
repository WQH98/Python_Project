import urllib.request

# url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=%E6%89%8B%E6%9C%BAedge%E6%8A%93%E5%8C%85%E6%96%AD%E7%BD%91&oq=%25E5%259B%25BE%25E7%2589%2587&rsv_pq=dacc3aac004fc6f5&rsv_t=9b0aqMrydcY3v5SfXp4zeB7ebcZvGeZnf%2FFzKGjNWwtbXmPtfrqC0CFNkdo&rqlang=cn&rsv_enter=1&rsv_dl=th_3&rsv_sug3=13&rsv_sug1=15&rsv_sug7=101&rsv_sug2=1&rsv_btype=t&rsp=3&rsv_sug9=es_0_1&inputT=8164&rsv_sug4=8161&rsv_sug=9'
# print(urllib.request.unquote(url))
# print(urllib.request.quote('测试'))

url = "http://www.baidu.com/s?"
wd = {
    "wd": "测试",
}
new_url = url + urllib.parse.urlencode(wd)
print(new_url)
res = urllib.request.urlopen(new_url)
print(res.read().decode('utf-8'))



