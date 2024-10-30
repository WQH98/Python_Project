const CryptoJS = require("crypto-js");

function get_sign() {
    let data = 'equtype=ANDROID&loginImei=Androidnull&timeStamp=1723423161816&userPwd=1234567890&username=15588547880&key=sdlkjsdljf0j2fsjk';
    return CryptoJS.MD5(data).toString().toUpperCase();
}

function get_data() {
    let data = '{"equtype":"ANDROID","loginImei":"Androidnull","sign":"' + get_sign() + '","timeStamp":"1723423161816","userPwd":"1234567890","username":"15588547880"}';
    console.log(data);

    let des_key = '65102933';
    let md5_des_key = CryptoJS.MD5(des_key).toString();
    console.log(md5_des_key);
    let key = CryptoJS.enc.Hex.parse(md5_des_key);
    let iv = CryptoJS.enc.Utf8.parse('32028092');
    let encrypted = CryptoJS.DES.encrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    console.log(encrypted.toString());
}

get_data();

