from pymongo import MongoClient

# 连接数据库
conn = MongoClient('localhost')

# 选择数据库 选择test库
db = conn.test

# insert_one
# 向文档中插入一条数据
# db.user.insert_one({'name': 'wangwu', 'age': '23', 'sex': 'w'})

# insert_many
# 向文档中插入多条数据
data = db.user.insert_many([{'name': 'zhaoliu', 'age': '23', 'sex': 'm'}, {'name': '赵六', 'age': '24', 'sex': 'w'}])
print(data)
# 获取插入返回的ID
print(data.inserted_ids)

# 关闭连接
conn.close()
