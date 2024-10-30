import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()
pid = redv.spawn(["com.hupu.shihuo"])
session = redv.attach(pid)

src = """
Java.perform(function() {
    // 包、类
    var UpdateDialog = Java.use("com.azhon.appupdate.dialog.UpdateDialog");

    // Hook，替换
    UpdateDialog.show.implementation = function() {
        console.log("-----------------请求来了！！！-----------------");

        // 执行原来的方法
        // var ret = this.show();
        // return ret;
    }
})
"""

script = session.create_script(src)


def on_message(message, data):
    print(message, data)


script.on('message', on_message)
script.load()
redv.resume(pid)
sys.stdin.read()
