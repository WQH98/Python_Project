import sys
import frida

# 连接手机设备
redv = frida.get_remote_device()
print(redv)


# 枚举所有的进程
processes = redv.enumerate_processes()
for process in processes:
    print(process)


# 获取在前台运行的APP
front_app = redv.get_frontmost_application()
print(front_app)
