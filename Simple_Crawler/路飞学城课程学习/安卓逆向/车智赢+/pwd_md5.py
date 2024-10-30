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
    SecurityUtil.encodeMD5.implementation = function(str) {
        console.log("-----------------请求来了！！！-----------------");
        console.log("明文", str);
        // 执行原来的方法
        var ret = this.encodeMD5(str);
        console.log("密文", ret);
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
