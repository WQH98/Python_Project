from pymongo import MongoClient

# 连接数据库
conn = MongoClient('localhost', 27017)

# 选择数据库
db = conn.test

# update_one
# 将name为lucky的数据的年龄累加1岁
# data = db.user.update_one({'name': 'lucky'}, {'$inc': {'age': 1}})
# # 匹配的行数 更改的行数
# print(data.matched_count, data.modified_count)

# update_many
# 将name为lucky的数据的年龄直接更改为18
data = db.user.update_many({'name': 'lucky'}, {'$set': {'age': 18}})
# 匹配的行数 更改的行数
print(data.matched_count, data.modified_count)

# 关闭数据库连接
conn.close()
