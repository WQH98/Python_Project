# 如果js代码中含有中文 则引入以下代码
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs

# 作用就一个 就是在python中执行js代码
js_code = "1 + 1"
# 作用就是运行一个js代码 特点是有返回值
r = execjs.eval(js_code)
print(r)


js_code2 = """
    function fn() {
        console.log("test");
        return 1 + 1;
    }
    fn();
"""
# 这个可以运行代码 但是没有返回值 所以基本不用
r = execjs.exec_(js_code2)
print(r)


# 最常用的一套方案
with open("01_测试execjs.js", mode='r', encoding='utf-8') as f:
    js_code3 = f.read()

# 先加载js代码
js = execjs.compile(js_code3)
# 调用fn1函数 相当于fn1()
r1 = js.call('fn1')
# 调用fn2函数 相当于fn2(2, 3)
r2 = js.call('fn2', 2, 3)
# 调用fn3函数 相当于fn3()
r3 = js.call('fn3')
print(r1, r2, r3)

