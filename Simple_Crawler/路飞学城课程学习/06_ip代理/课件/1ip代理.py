import requests
proxy = {
    'http': '122.9.101.6:8888'
}
'''
"origin": "125.33.247.111"
'''
# result = requests.get("http://httpbin.org/ip")

result = requests.get("http://httpbin.org/ip", proxies=proxy)
print(result.text)