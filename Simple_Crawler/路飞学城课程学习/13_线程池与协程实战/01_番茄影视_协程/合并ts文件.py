import os


def merge(path, filename='output'):
    os.chdir(path)
    cmd = f'ffmpeg -i new_index.m3u8 -c copy {filename}.mp4'
    os.system(cmd)


def change_m3u8(path):
    with open(f'{path}/index.m3u8', 'r') as f:
        lines = f.readlines()
    i = 0
    new_data = []
    for line in lines:
        if line.startswith('#'):
            new_data.append(line)
            continue
        line = f'{i}.ts'
        i += 1
        new_data.append(line + '\n')
    with open(f'{path}/new_index.m3u8', 'w') as f:
        f.writelines(new_data)


if __name__ == '__main__':
    path = './下载'
    change_m3u8(path)
    merge(path)
