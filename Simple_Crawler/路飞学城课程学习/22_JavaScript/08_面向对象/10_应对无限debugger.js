// js hook
// 1、记录一下以前的Function.prototype.constructor
var xxxx = Function.prototype.constructor;

// 2、给Function.prototype.constructor设置一个新的功能
Function.prototype.constructor = function() {
    // 3、判断参数是否是debugger
    if(arguments[0] === "debugger") {
        // 4、如果是debugger 就不构建函数
        return;
    }
    else {
        // 5、如果不是debugger 需要放行 继续执行原来本应该的操作
        return xxxx.apply(this, arguments);
    }
}

