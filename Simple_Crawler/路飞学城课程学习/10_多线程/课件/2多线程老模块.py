import time

import win32api
import _thread


def run():
    win32api.MessageBox(0, '人生苦短，我要学python', '消息',6)


if __name__ == '__main__':
    for i in range(4):
        _thread.start_new_thread(run, ())
    print('over')
    time.sleep(20)
