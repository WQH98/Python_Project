import time


def run(index):
    print("run start", index)
    time.sleep(2)
    print("run over", index)


for i in range(1, 5):
    run(i)
