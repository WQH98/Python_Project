import redis

# 1、连接
conn = redis.Redis(password='admin', decode_responses=True)

r = conn.get('name')
print(r)


