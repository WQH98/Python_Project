const crypto = require("crypto")

const d = "fanyideskweb"
  , u = "webfanyi"
  , p = "client,mysticTime,product"
  , m = "1.0.0"
  , h = "web"
  , g = "fanyi.web"
  , f = 1
  , b = 1
  , v = 1
  , A = "wifi"
  , y = 0;

function T(e) {
    return crypto.createHash("md5", "").update(e).digest()
}

function _(e) {
    return crypto.createHash("md5", "").update(e.toString()).digest("hex")
}

function S(e, t) {
    return _(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

function k(e, t) {
    const o = (new Date).getTime();
    return {
        sign: S(o, e),
        client: d,
        product: u,
        appVersion: m,
        vendor: h,
        pointParam: p,
        mysticTime: o,
        keyfrom: g,
        mid: f,
        screen: b,
        model: v,
        network: A,
        abtest: y,
        yduuid: t || "abcdefg"
    }
}

e = {
    dictResult: 'true',
    domain: "0",
    from: "auto",
    i : "hello worl",
    keyid: "webfanyi",
    to: "",
    useTerm: 'false',
};

val = k(e, 'fsdsogkndfokasodnaso')

console.log(val)
