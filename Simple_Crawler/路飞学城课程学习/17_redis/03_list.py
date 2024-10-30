import redis

# 连接数据库
r = redis.StrictRedis(password='admin', decode_responses=True)

# 从左侧添加值
# print(r.lpush('list', 1, 2, 3, 4))

# 获取值
# print(r.lrange('list', 0, -1))

# 从尾部添加值
# print(r.rpush('list', 5))
# print(r.lrange('list', 0, -1))

# pop弹出 左侧删除 头部删除
print(r.lrange('list', 0, -1))
print(r.lpop('list'))
print(r.lrange('list', 0, -1))

# 关闭数据库
r.close()
