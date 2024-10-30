from flask import Flask

app = Flask("test")

# 做一个绑定 浏览器有人访问某个url以后 自动执行该函数
# 把 / 和下面的函数进行绑定 有人访问 / 的时候 自动执行下面的函数
# 并把函数的返回值返回给浏览器
@app.route("/")
def test():
    name = "alex"
    gift = "穿云箭"
    with open("03_flask.html", mode='r', encoding='utf-8') as f:
        # 服务器端渲染 在服务器这边已经把数据和html整合在一起了
        page_source = f.read().replace("$$name$$", name).replace("$$gift$$", gift)
        return page_source


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4999)

