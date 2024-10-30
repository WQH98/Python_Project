import redis

# 创建redis
r = redis.StrictRedis(password='admin', decode_responses=True)

# # 设置 key value
# print(r.set('name', 'test'))
# # 读取
# print(r.get('name'))

# 批量设置
# print(r.mset({'age': 18, 'sex': 'man'}))
# 批量获取
# print(r.mget('name', 'age', 'sex'))

# getrange 获取name值索引0-1的值
# print(r.getrange('name', 0, 1))

# 输出类型
print(r.type('name'))


# 关闭连接
r.close()
