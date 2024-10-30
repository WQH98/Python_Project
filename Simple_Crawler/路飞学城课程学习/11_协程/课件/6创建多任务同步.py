import time

def run(url):
    print(f'向{url}抓取数据开始')
    time.sleep(2)
    print(f'向{url}抓取数据结束')


t1 = time.time()
for i in range(3):
    run(i)
print(time.time()-t1)