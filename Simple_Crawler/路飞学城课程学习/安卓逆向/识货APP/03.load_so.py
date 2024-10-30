import frida
import sys

redv = frida.get_remote_device()
pid = redv.spawn(["com.kmxs.reader"])
session = redv.attach(pid)


src = """
    Java.perform(function(){
        var dlopen = Module.findExportByName(null, "dlopen");
        var android_dlopen_ext = Module.findExportByName(null, "android_dlopen_ext");
        Interceptor.attach(dlopen, {
            onEnter: function(args) {
                var path_ptr = args[0];
                var path = ptr(path_ptr).readCString();
                console.log("[dlopen:]", path);
            },
            onLeave: function(retval) {
            
            }
        });
        Interceptor.attach(android_dlopen_ext, {
            onEnter: function(args) {
                var path_ptr = args[0];
                var path = ptr(path_ptr).readCString();
                console.log("[dlopen_ext:]", path);
            },
            onLeave: function(retval) {
            
            }
        });
    })
"""

script = session.create_script(src)


def on_message(message, data):
    print(message, data)


script.on('message', on_message)
script.load()
redv.resume(pid)
sys.stdin.read()

