import threading
import time
import requests

finished_flag = True
proxies = {'http': "socks5://127.0.0.1:8080",
           'https': "socks5://127.0.0.1:8080"}

def print_numbers():
    global finished_flag
    url = "https://service.ipzan.com/core-extract?num=1&no=20230930146331307287&minute=1&format=txt&protocol=1&pool=quality&mode=whitelist&secret=daogee708nejt4g"
    while finished_flag:
        resp = requests.get(url)
        if resp.status_code == 200:
            proxies["http"] = resp.text
            proxies["https"] = resp.text
        print("resp: ", resp.text)
        time.sleep(40)

if __name__ == '__main__':
    thread = threading.Thread(target=print_numbers)
    thread.start()
    for i in range(300):
        print(i, proxies["http"], proxies["https"])
        time.sleep(1)
    finished_flag = False
