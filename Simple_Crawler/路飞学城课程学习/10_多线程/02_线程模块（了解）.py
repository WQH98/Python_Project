import _thread
import time

import win32api


def run():
    win32api.MessageBox(0, "test1", "ceshi2", 6)


_thread.start_new_thread(run, ())
time.sleep(10)
print('over')
