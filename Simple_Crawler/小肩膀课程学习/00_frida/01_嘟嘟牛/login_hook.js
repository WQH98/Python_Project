
// 如果是Java hook代码 都放到 perform 中
Java.perform(function() {

    // let LoginActivity = Java.use("com.dodonew.online.ui.LoginActivity");
    // LoginActivity.login.implementation = function(username, pwd) {
    //     console.log("login---->username:", username);
    //     console.log("login---->pwd:", pwd);
    //     this.login(username, pwd);
    // }

    // let JsonRequest = Java.use("com.dodonew.online.http.JsonRequest");
    // JsonRequest.addRequestMap.overload('java.util.Map', 'int').implementation = function(addMap, a) {
    //     let addMap_cast = Java.cast(addMap, Java.use("java.util.HashMap"));
    //     console.log("addRequestMap---->addMap:", addMap_cast);
    //     console.log("addRequestMap---->a:", a);
    //     this.addRequestMap(addMap, a);
    // }


    /*
    *   String code = RequestUtil.paraMap(addMap, Config.BASE_APPEND, "sign");
    *   addMap: {timeStamp=1723275874059, loginImei=Androidnull, equtype=ANDROID, userPwd=1234567890, username=15588547880}
    *   append: sdlkjsdljf0j2fsjk
    *   res: {"equtype":"ANDROID","loginImei":"Androidnull","sign":"B262E907687BA6C579845349C16BA343","timeStamp":"1723275874059","userPwd":"1234567890","username":"15588547880"}
    *   在这个函数里面 传入的值里面加了个sign
    *   sign是一个标准的MD5 32位大写加密
    *   是对equtype=ANDROID&loginImei=Androidnull&timeStamp=1723276438048&userPwd=1234567890&username=15588547880&key=sdlkjsdljf0j2fsjk
    *   进行的加密
    * */
    let RequestUtil = Java.use("com.dodonew.online.http.RequestUtil");
    RequestUtil.paraMap.overload('java.util.Map', 'java.lang.String', 'java.lang.String').implementation = function(addMap, append, sign) {
        let addMap_cast = Java.cast(addMap, Java.use("java.util.HashMap"));
        console.log("paraMap---->addMap:", addMap_cast);
        console.log("paraMap---->append:", append);
        console.log("paraMap---->sign:", sign);
        let res = this.paraMap(addMap, append, sign);
        console.log("paraMap---->res:", res);
        return res;
    }
    RequestUtil.encodeDesMap.overload('java.lang.String', 'java.lang.String', 'java.lang.String').implementation = function(data, desKey, desIV) {
        console.log("encodeDesMap---->data:", data);
        console.log("encodeDesMap---->desKey:", desKey);
        console.log("encodeDesMap---->desIV:", desIV);
        let res = this.encodeDesMap(data, desKey, desIV);
        console.log("encodeDesMap---->res:", res);
        return res;
    }

    let Utils = Java.use("com.dodonew.online.util.Utils");
    Utils.md5.implementation = function(string) {
        console.log("md5---->string:", string);
        let res = this.md5(string);
        console.log("md5---->res:", res);
        return res;
    }
})


