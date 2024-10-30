Java.perform(function() {
    let yz1 = Java.use("yz1");
    yz1.b.implementation = function(request) {
        console.log("request: ", request);
        let resp = this.b(request);
        console.log("resp: ", resp);
        return resp;
    }

    let go2 = Java.use("go2");
    go2.k.implementation = function() {
        let resp = this.k();
        console.log("go2", resp);
        return resp;
    }

    let CoinSignBean = Java.use("com.bailing.lib_api.coin.CoinSignBean")
    CoinSignBean.hashCode.implementation = function() {
        let resp = this.hashCode();
        console.log("hashCode", resp);
        return resp;
    }

    let Request = Java.use("okhttp3.Request")
    Request.toString.implementation = function() {
        let resp = this.toString();
        console.log("toString", resp);
        return resp;
    }
})
