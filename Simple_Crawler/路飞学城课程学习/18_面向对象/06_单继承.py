class A:
    money = 10000

    def speak(self):
        print('我有很多钱', self.money)


# B类继承A类
class B(A):
    money = 10000

    def run(self):
        print('跑的很快 尤其是被狗追的时候')

    # 对于父类中的speak方法的重写
    # 调用父类中的方法
    def speak(self):
        # 重新调用父类的方法 speak
        super(B, self).speak()
        # 重新调用父类的方法 speak
        A.speak(self)
        # 补充我自己的想法
        print('我是B中的speak')


b = B()
print(b.money)
print(b.speak())



