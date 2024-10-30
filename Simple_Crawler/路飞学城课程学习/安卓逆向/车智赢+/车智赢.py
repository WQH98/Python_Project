import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()

# Hook手机上的那个APP（APP的包的名字）
session = redv.attach("车智赢+")

src = """
Java.perform(function() {
    // 包、类
    var UserModel = Java.use("com.che168.autotradercloud.user.model.UserModel");

    // Hook，替换
    UserModel.loginByPassword.implementation = function(str, str2, str3, str4, str5, responseCallback) {
        console.log("-----------------请求来了！！！-----------------");
        console.log("用户名", str2);
        console.log("密码", str3);
        // console.log(str, str2, str3, str4, str5, responseCallback);
        // 执行原来的方法
        var ret = this.loginByPassword(str, str2, str3, str4, str5, responseCallback);
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
