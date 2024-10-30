import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()

# Hook手机上的那个APP（APP的包的名字）
session = redv.attach("油联合伙人")

src = """
    Java.perform(function() {
        // 包、类
        var presenter = Java.use("com.yltx.oil.partner.modules.login.presenter.LoginPresenter");
        var Md5 = Java.use("com.yltx.oil.partner.utils.Md5");
        // Hook，替换
        presenter.submitLogin.implementation = function(str,str2) {
            console.log(str,str2);
            // 执行原来的方法
            var ret = this.submitLogin(str,str2);
            // return ret;
        }
        Md5.md5.implementation = function(str) {
            // 执行原来的方法
            var ret = this.md5(str);
            console.log("明文",str);
            console.log("密文",ret);
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

"""
注意事项：
    目前运行Hook脚本时候 应用进程必须放在前台运行中
    
"""
