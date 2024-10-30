from flask import Flask, render_template, request

app = Flask("Test")


@app.route("/")
def index():
    name = "alex"
    gift = "穿云箭"
    return render_template("01_index.html", name=name, gift=gift)


@app.route("/test1")
def test1():
    ua = request.headers.get("User-Agent")
    if 'python' in ua:
        return "UA有问题 这不是一个好的爬虫"
    ck = request.cookies.get("alex")
    if ck != 'sb':
        return "CK有问题 这不是一个好的爬虫"
    # 要接收到两个参数 所有在url上的参数 都必须用args来接收
    name = request.args.get("name")
    age = request.args.get("age")
    if name and age:
        return "正常的返回一个数据"
    else:
        return "未知错误 参数不正确"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4999)
