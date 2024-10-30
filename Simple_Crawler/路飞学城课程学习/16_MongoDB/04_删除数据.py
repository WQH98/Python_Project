from pymongo import MongoClient

# 连接数据库
conn = MongoClient('localhost', 27017)

# 选择数据库
db = conn['test']

# delete_one  删除一条
# 删除年龄大于50的一条数据
# data = db.user.delete_one({'age': {'$gt': 50}})
# # 打印删除的条数
# print(data.deleted_count)

# delete_many  删除多条
# 删除年龄小于30的所有数据
data = db.user.delete_many({'age': {'$lt': 30}})
# 打印删除的条数
print(data.deleted_count)

# 关闭数据库
conn.close()
