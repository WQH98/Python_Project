import threading

# 创建一把锁
lock = threading.Lock()
# print(lock.acquire())  # 上锁  True
# print(lock.release())  # 解锁  None


print(lock.acquire())  # 上锁  True
print(lock.acquire())  # 上锁  True
print('已经上锁了', 1)
print(lock.release())  # 解锁  None
print('over', 2)