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
    }
    
    var Builder = Java.use("okhttp3.OkHttpClient$Builder");
    Builder.addInterceptor.implementation = function(obj) {
        console.log(JSON.stringify(obj));
        var res = this.addInterceptor(obj);
        return res;
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
