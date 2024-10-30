import threading

# 创建一把锁
lock = threading.Lock()
print(lock)

# 上锁
print(lock.acquire())
# 刚刚上的锁 还没有解开 
# print(lock.acquire())

# 解锁
print(lock.release())
