import time
import _thread


def run():
    print('run开始')
    time.sleep(5)
    print('run结束')



if __name__ == '__main__':
    for i in range(5):
        _thread.start_new_thread(run, ())
    print('over')
    # time.sleep(100)