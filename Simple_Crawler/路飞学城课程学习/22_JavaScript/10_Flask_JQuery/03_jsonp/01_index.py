import flask

app = flask.Flask("app")

@app.route("/")
def index():
    name = 'alex'
    gift = '穿云箭'
    return flask.render_template("01_index.html", name=name, gift=gift)


@app.route("/test1")
def test1():
    # 获取到callback的值
    cb = flask.request.args.get("callback")
    return cb + "('" + '这是一个测试' + "')"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4999)

