def test():
    for i in range(10):
        yield i


t = test()
# print(next(t))
# print(next(t))
for i in t:
    print(i)