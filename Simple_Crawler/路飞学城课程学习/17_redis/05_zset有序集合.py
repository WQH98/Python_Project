import redis

# 创建连接
r = redis.StrictRedis(password='admin', decode_responses=True)

# 添加值 zadd
# print(r.zadd('zadd', {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}))

# 获取元素个数
# print(r.zcard('zadd'))

# 返回元素对应的权重
# print(r.zscore('zadd', 'a'))

# 设置过期时间
# print(r.expire('zadd', 1000))

# 取消过期时间
# print(r.persist('zadd'))

# 关闭连接
r.close()
