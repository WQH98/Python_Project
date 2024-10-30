# 题目：模仿静态变量的用法。
# 程序分析：无。

def varfun():
    var = 0
    print("var = %d" % var)
    var += 1


if __name__ == '__main__':
    for i in range(3):
        varfun()


# 类的属性
class Static:
    ststicVar = 5

    def varfun(self):
        self.ststicVar += 1
        print(self.ststicVar)


print(Static.ststicVar)
a = Static()
for i in range(3):
    a.varfun()
