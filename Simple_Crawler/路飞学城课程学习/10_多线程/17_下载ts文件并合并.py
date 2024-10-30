import os

import requests
from concurrent.futures import ThreadPoolExecutor, wait

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}


def download_one_video(url, i):
    print(url, i, "开始下载")
    response = requests.get(url, headers=headers)
    with open(f'./美剧视频下载/{i}.ts', 'wb') as f:
        f.write(response.content)
    print(url, i, "完成下载")


def download_all_video():
    with open('16_second_m3u8_url.txt', 'r') as f:
        data = f.readlines()
    # 创建线程池 开20个
    pool = ThreadPoolExecutor(20)
    tasks = []
    i = 0
    for line in data:
        # 提取ts的url路径
        if line.startswith('#'):
            continue
        # 使用strip去除url结尾的换行符
        ts_url = line.strip()
        tasks.append(pool.submit(download_one_video, ts_url, i))
        i += 1
    # 集体等待创建的线程对象执行完毕
    wait(tasks)


def merge(path, filename='output'):
    '''
    进行ts文件合并 解决视频音频不同步的问题 建议使用这种
    :param filePath:
    :return:
    '''
    os.chdir(path)
    cmd = f'ffmpeg -i test.m3u8 -c copy {filename}.mp4'
    os.system(cmd)


if __name__ == '__main__':
    merge('./美剧视频下载')
