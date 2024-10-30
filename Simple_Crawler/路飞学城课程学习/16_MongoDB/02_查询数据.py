from bson import ObjectId
from pymongo import MongoClient

# 连接数据库
conn = MongoClient('localhost')

# 选择数据库
db = conn.test

# 查询所有
# datas = db.user.find()

# 查询name为lucky的数据
# datas = db.user.find({'name': 'lucky'})

# 按照ID进行查询 需要注意 ObjectId 要进行导入
# datas = db.user.find({'_id': ObjectId('662debf6ca16c03ddc46b79a')})

# sort排序 以年龄排序
# 升序
# datas = db.user.find().sort({'age', 1})
# 降序
# datas = db.user.find().sort({'age', -1})

# 查询年龄大于23的并且降序
# datas = db.user.find({'age': {'$gt': 23}}).sort({'age', -1})

# 降序 只取出前两条数据
# datas = db.user.find().sort({'age': -1}).limit(2)

# 降序 跳过两条取两条
# datas = db.user.find().sort({'age': -1}).skip(2).limit(2)

# 模糊查询 name中带有l的数据
datas = db.user.find({'name': {'$regex': 'l'}})

for data in datas:
    print(data)

# 断开数据库
conn.close()

