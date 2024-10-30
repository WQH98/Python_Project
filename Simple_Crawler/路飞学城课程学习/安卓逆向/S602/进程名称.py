# 需要先做端口转发 才可以使用脚本连接手机
# adb forward tcp:27042 tcp:27042
# adb forward tcp:27043 tcp:27043
import frida

# 获取设备信息(USB线)
redv = frida.get_remote_device()

# 获取在前台运行的APP(画面现在打开的APP)
front_app = redv.get_frontmost_application()
print(front_app)
