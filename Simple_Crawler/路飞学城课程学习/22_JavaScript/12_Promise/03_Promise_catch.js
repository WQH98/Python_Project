/*
*   执行 reject 时，Promise 状态从 pending 变为 rejected
*   会执行 catch 方法，catch 方法接收的也是一个函数
*   函数中携带一个参数，该参数为 reject(err) 返回的数据。
* */

var p = new Promise(function(resolve, reject) {
    setTimeout(() => {
        resolve('success message');
        reject('error message');
    }, 1000);
}).then(res => {
    console.log('success', res);
}).catch(err => {
    console.log('err', err);
})

var res1 = function() {
    console.log('test1')
}
var res2 = function() {
    console.log('test2')
}
var res3 = function() {
    console.log('test3')
}
Promise.resolve(res1).then(res2, res3);
