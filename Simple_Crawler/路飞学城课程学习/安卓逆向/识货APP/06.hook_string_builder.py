import frida
import sys

redv = frida.get_remote_device()

session = redv.attach("识货")

src = """
Java.perform(function() {
    var StringBuilder = Java.use("java.lang.StringBuilder");
    StringBuilder.toString.implementation = function() {
        var res = this.toString();
        console.log(res);
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
