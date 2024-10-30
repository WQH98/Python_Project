# 模块可以向外部提供全局变量 函数 类
# 注意：直接执行的代码不是向外界提供的工具
# 文件被导入时 能够直接执行的代码不需要被执行
def say_hello():
    print("你好 你好 我是 say hello")


if __name__ == "__main__":
    # 如果直接执行程序 得到的结果就是__main__
    print(__name__)


    print("小明开发的模块")
    say_hello()
