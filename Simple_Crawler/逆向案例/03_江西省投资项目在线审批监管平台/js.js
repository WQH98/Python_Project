var test1 = function(sig) {
    sig = String(sig)

    var chars = "0123456789abcdef";
    curUrl = "/icity/api-v2/jxtzxm.app.icity.ipro.IproCmd/getDisplayListByPage"

    var key = "";
    var keyIndex = -1;
    for(var i=0;i<6;i++){
        var c=sig.charAt(keyIndex+1);
        key +=c;
        keyIndex = chars.indexOf(c);
        if(keyIndex<0 || keyIndex>=sig.length){
            keyIndex = i;
        }
    }

    var timestamp = parseInt(Math.random()*(9999-1000+1)+1000)+"_"+key+"_"+Date.parse(new Date());

    var tkey = "";
    var tkeyIndex = -1;
    for(var i=0;i<6;i++){
        var c=timestamp.charAt(tkeyIndex+1);
        tkey +=c;
        tkeyIndex = chars.indexOf(c);
        if(tkeyIndex<0 || tkeyIndex>=timestamp.length){
            tkeyIndex = i;
        }
    }

    var t = timestamp;
    t = t.replace(/\+/g,"_");
    curUrl+= "?s=" + sig;
    curUrl+= "&t=" +  t;
    curUrl+= "&o=" + tkey;

    return curUrl;
}

