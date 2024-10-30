var crypto_js = require('crypto-js');

function hash(encode_mode, encode_data) {
    if(encode_mode === "md5") {
        return crypto_js.MD5(encode_data).toString();
    }
    if(encode_mode === "sha1") {
        return crypto_js.SHA1(encode_data).toString();
    }
    if(encode_mode === "sha256") {
        return crypto_js.SHA1(encode_data).toString();
    }
}


function hash_encode(data) {

    var chars_length = data["chars"]["length"];
    for(let i = 0; i < chars_length; i++) {
        for(let j = 0; j < chars_length; j++) {
            let cookie = data["bts"][0] + data["chars"]["substr"](i, 1) + data["chars"]["substr"](j, 1) + data["bts"][1];
            if(hash(data["ha"], cookie) === data["ct"]) {
                // console.log(cookie);
                return cookie;
            }
        }
    }
}

// hash_encode({
//     "bts":["1718623120.713|0|0Ji","NpHgWVOdwU4zNzFTvvMvm4%3D"],
//     "chars":"stedjhPmxePYOUGMiiSdqv",
//     "ct":"a46e9861720265005bdffbf3b04e424d",
//     "ha":"md5",
//     "is":true,
//     "tn":"__jsl_clearance_s",
//     "vt":"3600",
//     "wt":"1500"
// });

