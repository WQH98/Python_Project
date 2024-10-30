import random

# 会搜索当前目录指定模块名的文件 如果有就直接导入
# 如果没有 再搜索系统目录
# 在开发时 给文件起名 不要和系统的模块文件重名
# Python中每一个模块都有一个内置属性__file__可以查看模块的完整路径

print(random.__file__)

rand = random.randint(1, 10)
print(rand)
