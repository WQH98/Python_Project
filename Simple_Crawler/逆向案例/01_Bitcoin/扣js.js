API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"

let encryptTime = function(t) {
    var e = (1 * t + 1111111111111).toString().split("")
      , n = parseInt(10 * Math.random(), 10)
      , o = parseInt(10 * Math.random(), 10)
      , r = parseInt(10 * Math.random(), 10);
    return e.concat([n, o, r]).join("")
}

let encryptApiKey = function() {
    var t = API_KEY
      , e = t.split("")
      , n = e.splice(0, 8);
    return t = e.concat(n).join("")
}

let comb = function(t, e) {
    var n = "".concat(t, "|").concat(e);
    return btoa(n)
}


let getApiKey = function() {
    var t = (new Date).getTime()
      , e = encryptApiKey();
    return t = encryptTime(t),
    comb(e, t)
}

console.log(getApiKey())
