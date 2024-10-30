import pymysql
from pymysql.cursors import DictCursor


# 1、创建连接
conn = pymysql.connect(user='root', password='admin', host='localhost', database='test')

# 2、没有任何一个语言是直接操作MySQL的 要通过游标cursor来执行
cursor = conn.cursor(DictCursor)
cursor.execute('select * from class')
# 拿到结果
r = cursor.fetchall()
print(r)

# 插入一条语句
name = '三年二班'
money = 600
banzhuren = '周杰伦'
# 这种sql插入的方式 首先是很乱 其次是有被注入的风险
# sql = f'insert into class(cname, cmoney, cbanzhuren) values ("{name}", {money}, "{banzhuren}")'
# print(sql)
# cursor.execute(sql)

# 第二种sql插入的方式
sql = 'insert into class(cname, cbanzhuren, cmoney) values (%s, %s, %s)'
# 这种处理方案 能避免sql注入的问题
cursor.execute(sql, (name, banzhuren, money))  # 这里给的是元祖

# 数据提交
conn.commit()

# 拿到结果
r = cursor.fetchall()
print(r)
# 关闭连接
conn.close()

