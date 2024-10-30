from flask import Flask, render_template, request, json

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


# 默认只支持get methods=["post"]才支持post
@app.route("/test2", methods=["post"])
def test2():
    # form data必须用form来接受
    name = request.form.get("name")
    hobby = request.form.get("hobby")
    if name and hobby:
        return json.dumps({"code": 0, "data": {"name": name, "hobby": hobby}})
    else:
        return json.dumps({"code": 999,"msg": "不是个合格的爬虫", "data": {}})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4999)
