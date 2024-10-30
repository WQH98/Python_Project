import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()

# Hook手机上的那个APP（APP的包的名字）
session = redv.attach("识货")

src = """
Java.perform(function() {
    // 包、a
    var a = Java.use("cn.shihuo.modulelib.startup.core.c.a");

    // Hook，替换
    a.intercept.implementation = function(chain) {
        console.log("-----------------请求来了！！！-----------------");
        var request = chain.request();
        var url_string = request.url().toString();
        if(url_string.indexOf("https://sh-gateway.shihuo.cn/v4/services/sh-goodsapi/app_swoole_shoe/preload/single") !== -1) {
            console.log(url_string);
        }
        var res = this.intercept(chain);
        return res;
    }
})
"""

script = session.create_script(src)


def on_message(message, data):
    print(message)


script.on('message', on_message)
script.load()
sys.stdin.read()
