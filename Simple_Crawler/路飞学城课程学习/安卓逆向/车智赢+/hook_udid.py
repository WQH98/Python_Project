import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()

# Hook手机上的那个APP（APP的包的名字）
session = redv.attach("车智赢+")

src = """
Java.perform(function() {
    // 包、类
    var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil");

    // Hook，替换
    SecurityUtil.encode3Des.implementation = function(context, str) {
        console.log("-----------------请求来了！！！-----------------");
        console.log("明文")
        console.log("context = ", context)
        console.log("str = ", str)
        // 执行原来的方法
        var ret = this.encode3Des(context, str);
        console.log("密文")
        console.log("udid = ", ret)
        return ret;
    }
})
"""

script = session.create_script(src)


def on_message(message, data):
    print(message)


script.on('message', on_message)
script.load()
sys.stdin.read()
