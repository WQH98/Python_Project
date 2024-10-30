import frida
import sys

redv = frida.get_remote_device()

session = redv.attach("识货")

src = """
    Java.perform(function() {
        var Base64 = Java.use("android.util.Base64");
        Base64.encodeToString.overload('[B', 'int').implementation = function(bArr, val) {
            var res = this.encodeToString(bArr, val);
            console.log("加密了-->", res);
            // 查看调用栈
            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()));
            return res;
        }
    })
"""

script = session.create_script(src)


def on_message(message, data):
    print(message, data)


script.on('message', on_message)
script.load()
sys.stdin.read()
