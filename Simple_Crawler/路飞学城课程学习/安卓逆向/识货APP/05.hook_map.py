import frida
import sys

redv = frida.get_remote_device()
pid = redv.spawn(["com.hupu.shihuo"])
session = redv.attach(pid)

src = """
Java.perform(function() {
    // 包、类
    var UpdateDialog = Java.use("com.azhon.appupdate.dialog.UpdateDialog");

    // Hook，替换
    UpdateDialog.show.implementation = function() {
        // 关掉所有的弹窗 包括更新的弹窗
        console.log("-----------------请求来了！！！-----------------");
    }
    var TreeMap = Java.use("java.util.TreeMap");
    TreeMap.put.implementation = function(key, value) {
        if(key == "data") {
            console.log(key, value);
        }
        var res = this.put(key, value);
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
