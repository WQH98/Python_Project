import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()

# Hook手机上的那个APP（APP的包的名字）
session = redv.attach("车智赢+")

src = """
Java.perform(function() {
    // 包、类
    var LaunchModel = Java.use("com.che168.autotradercloud.launch.model.LaunchModel");

    // Hook，替换
    LaunchModel.lambda$initRequestCommonParams$0.implementation = function(i, treeMap) {
        console.log("-----------------请求来了！！！-----------------");
        console.log("treeMap=", treeMap);
        // 执行原来的方法
        var ret = this.lambda$initRequestCommonParams$0(i, treeMap);
        console.log("ret treeMap=", ret);
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
