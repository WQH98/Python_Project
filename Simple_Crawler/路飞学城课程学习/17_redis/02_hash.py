import redis

# 创建redis
r = redis.StrictRedis(password='admin', decode_responses=True)

# # 设置hash
# print(r.hset('hash', 'name', 'lucky'))
# # 获取key为hash name字段的值
# print(r.hget('hash', 'name'))

# 获取所有 hash就是字典
# print(r.hgetall('hash'))

# 批量设置键值
# print(r.hmset('hash', {'name': 'tom', 'age': 18, 'sex': 'man'}))

# 批量获取
# print(r.hmget('hash', 'name', 'age', 'sex'))

# 获取hash所有的key
# print(r.hkeys('hash'))

# 获取hash所有的值
# print(r.hvals('hash'))

# 删除键值
# print(r.hkeys('hash'))
# print(r.hdel('hash', 'name'))
# print(r.hkeys('hash'))

r.close()
