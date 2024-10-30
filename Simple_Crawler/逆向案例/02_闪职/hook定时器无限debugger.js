// 好像有点问题 后面再尝试一下

let xxxxxx = setInterval;

setInterval = function(a, b) {
    if(a === 'debugger') {
        return;
    }
    else {
        return xxxxxx;
    }
}

