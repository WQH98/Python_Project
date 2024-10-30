import redis

# 创建redis
r = redis.StrictRedis(password='admin', decode_responses=True)

# sadd 添加数据
# print(r.sadd('set', 'a', 'b', 'c'))
# print(r.sadd('set1', 'a', 'b', 'd'))

# 获取值
# print(r.smembers('set'))

# 获取元素个数
# print(r.scard('set'))

# 查看交集
# print(r.sinter('set', 'set1'))

# 差集
# print(r.sdiff('set', 'set1'))

# 返回随机元素
print(r.srandmember('set'))  # 默认随机返回一个元素
print(r.srandmember('set', 2))  # 随机返回两个元素

# 关闭连接
r.close()
