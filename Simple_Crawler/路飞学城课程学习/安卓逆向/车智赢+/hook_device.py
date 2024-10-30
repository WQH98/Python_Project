import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()

# Hook手机上的那个APP（APP的包的名字）
session = redv.attach("车智赢+")

# 经过测试 好像不走这个地方
# 如果遇到代码不报错 而且没有输出的情况
# 1、代码逻辑找的不对 不会运行到这段代码
# 2、将手机软件关掉 重启 清除缓存
src = """
    Java.perform(function() {
        // 包、类
        var SPUtils = Java.use("com.che168.autotradercloud.util.SPUtils");
        
        // Hook，替换
        SPUtils.getDeviceId.implementation = function() {
            console.log("-----------------请求来了！！！-----------------");
            // 直接返回一个随机值
            return "253623";
        }
    });
"""

script = session.create_script(src)


def on_message(message, data):
    print(message)


script.on('message', on_message)
script.load()
sys.stdin.read()


