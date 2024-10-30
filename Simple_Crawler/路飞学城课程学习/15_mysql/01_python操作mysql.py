import pymysql


# 开始连接数据库
db = pymysql.connect(host='localhost', user='root', password='admin', database='wuqi')

# 设置字符编码
db.set_charset('utf8')

# 创建游标对象 用于增删改查
cursor = db.cursor()

"""
# 查询操作
# 执行sql语句
sql = 'select * from user'
cursor.execute(sql)
# 获取所有数据
data = cursor.fetchall()
print(data)
"""

try:
    # 插入操作 注意：字符串类型给引号
    # 执行sql语句
    # 在数据库中增加一条数据
    # sql = 'insert into user values(null, "王五", 20, 1)'
    # 修改username为王五的id改为7
    # sql = 'update user set id=7 where username="王五"'
    # 删除username为王五的数据
    sql = 'delete from user where username="王五"'
    cursor.execute(sql)
    # 查看受影响的行数
    print(cursor.rowcount)
    # 提交到数据库中
    db.commit()
except Exception as e:
    print(e)
    # 回滚
    db.rollback()
