import requests


url = "http://httpbin.org/ip"

proxies = {
    'http': '117.57.93.230:8089'
}

# res = requests.get(url, proxies=proxies)
res = requests.get(url)

print(res.content.decode())



