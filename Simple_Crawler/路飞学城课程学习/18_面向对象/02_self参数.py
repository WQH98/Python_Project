class Test:
    # 属性
    name = 'lucky'

    # 方法
    def speak(self):
        print('self', self)
        print('lucky is a good man')
        return 'lucky'


t = Test()
# 调用Test类中的属性
# print(t.name)
print(t.speak())
print('t', t)

