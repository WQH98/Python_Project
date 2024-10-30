class Test:
    name = 'lucky'
    # 初始化当前对象的
    # 可以在实例化的时候 自动传递一些参数

    def __init__(self, host, port, user):
        # 对象属性
        self.host = host
        self.port = port
        self.user = user
        # 临时变量 只有函数内部可以使用 就是正常的函数的局部变量
        sex = 'w'


t = Test(host='127.0.0.1', port=3306, user='root')
print(t.__dict__)
# 类属性
Test.aaa = 'aaa'
print(Test.__dict__)
# 这样也可以直接用
print(t.aaa)
print(t.__dict__)
