window = global
const JSEncrypt = require("jsencrypt");

var doLogin = function() {
    var password_old = 'test1234567890';
    var encrypt = new JSEncrypt();
    var public_key = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDaP+rYm6rqTMP565UmMU6YXq46KtAN3zwDSO8LNa15p0lJfsaY8jXY7iLsZqQZrGYr2Aayp6hYZy+Q+AMB/VUiSpD9ojPyOQ7r9jsf9jZbTOL4kj6iLZn37fEhp4eLvRgy5EJCyQoFyLCsgLechBTlYl2eA95C3j4ZUFhiV6WFHQIDAQAB';
    encrypt.setPublicKey(public_key);
    var pass_new = encrypt.encrypt(password_old);
    return pass_new;
}



// function doLogin() {
//     var password_old = $("#MemberPassword").val();
//     var encrypt = new JSEncrypt();
//     var public_key = $("#pk").val();
//     encrypt.setPublicKey(public_key);
//     var pass_new = encrypt.encrypt(password_old);
//     $("#MemberPassword").val(pass_new);
//     $("#login_button").submit()
// }


